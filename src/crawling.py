import os
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from src.utils import load_yaml, split_accessory
from dotenv import load_dotenv
from src import auction_dict
from datetime import datetime, timezone, timedelta

load_dotenv()
lark_api_key = 'bearer ' + os.environ.get('lark_api_key')


def lark_request(method, url, parameters=None):
    while True:
        if method == 'post':
            response = requests.post(url, headers={"authorization": lark_api_key}, json=parameters)
        elif method == 'get':
            response = requests.get(url, headers={"authorization": lark_api_key})
        else:
            return
        print(response.status_code)
        print(response.headers)
        print(response.text)
        if response.status_code == 200:
            responseDict = json.loads(response.text)
            return responseDict
        elif response.status_code == 429:
            time.sleep(int(response.headers['retry-after']) + 1)
            continue
        else:
            print(f'{response.status_code} error')
            return


def get_characterInfo(characterName):
    url = 'https://lostark.game.onstove.com/Profile/Character/'
    response = requests.get(url + characterName)
    soup = BeautifulSoup(response.text, 'html.parser')
    profile = soup.select_one('div.profile-ingame')
    if profile.select_one('div.profile-attention'):
        print(f'{characterName} 캐럭터 정보가 없습니다')
        return

    _class = profile.select_one('div.profile-equipment__character > img')['alt']
    itemLV = profile.select('div.level-info2__item > span')[1].text.replace('Lv.', '').replace(',', '')
    battleLV = profile.select('div.level-info__item > span')[1].text.replace('Lv.', '')
    expeditionLV = profile.select('div.level-info__expedition > span')[1].text.replace('Lv.', '')
    power = profile.select_one('div.profile-ability-basic > ul > li:nth-child(1) > span:nth-child(2)').text
    vitality = profile.select_one('div.profile-ability-basic > ul > li:nth-child(2) > span:nth-child(2)').text

    engraving = [engraving.text for engraving in profile.select('div.profile-ability-engrave > div > div > ul > li > span')]
    engraving_detail = ','.join(engraving)
    engraving_simple = re.sub(r'[^0-9]', '', engraving_detail)
    del engraving

    stat = [stat.text for stat in profile.select('div.profile-ability-battle > ul > li > span')]
    stat = [f'{stat[i]} {stat[i + 1]}' for i in range(0, len(stat), 2) if stat[i] in ['치명', '특화', '신속']]
    stat = ','.join(stat)

    card = profile.select('div.profile-card__text > div > ul > li > div.card-effect__title')[-1].text
    card = card.replace(')', '').replace(' (', ',').replace('성합계', '')
    card = re.sub(r' .세트', '', card)

    script = profile.select_one('script').text.replace(';', '').replace('$.Profile = ', '').strip()
    script = json.loads(script)
    del profile

    gems, equipment, equipment_name, accessory = {}, [], [], []
    for equip in script['Equip'].values():
        typeValue = re.sub('<.*?>', '', equip['Element_000']['value'])
        if typeValue.split()[-1] == '보석':
            gem = typeValue.replace('레벨 ', '')[:-5]
            if gem in gems:
                gems[gem] += 1
            else:
                gems[gem] = 1
        elif typeValue[0] == '+':
            equipType = typeValue.split()[-1]
            equipStep = typeValue[1:typeValue.find(' ')]
            equipName = typeValue[typeValue.find(' ') + 1:]
            equipLevel = ''
            for k, v in equipSetLevel.items():
                for setName in v:
                    if setName in equipName:
                        equipLevel = k
                        break
                else:
                    continue
                break
            equipQuality = equip['Element_001']['value']['qualityValue']
            equipment.append(f'{equipType}/{equipStep}/{equipLevel}/{equipQuality}')
            equipment_name.append(equipName)
        elif typeValue.split()[-1] in ['목걸이', '귀걸이', '반지']:
            # accType = typeValue.split()[-1]
            accGrade, accType = re.sub('<.*?>', '', equip['Element_001']['value']['leftStr0']).split()
            accQuality = equip['Element_001']['value']['qualityValue']
            accNature = '/'.join(re.sub('[^가-힣\s]', '', equip['Element_005']['value']['Element_001']).split())
            accEngraving = []
            for i in range(2):
                engraving = equip['Element_006']['value']['Element_000']['contentStr']['Element_00' + str(i)]['contentStr']
                engraving = ''.join(re.findall('(?<=>)[가-힣\s:]+(?=<)|\+\d{1}', engraving))
                accEngraving.append(engraving)
            accEngraving = '_'.join(accEngraving)
            accessory.append(f'{accType}/{accGrade}/{accQuality}/{accEngraving}/{accNature}')

    if gems:
        gems = sorted(gems.items(), key=lambda x: (-int(re.search(r'\d+', x[0]).group()), x[0][-1]))

    gem_simple = ','.join(f'{key} x{value}' for key, value in gems)
    equipment = ','.join(equipment)
    equipment_name = ','.join(equipment_name)
    accessory = ','.join(accessory)

    character_data = {
        'name': characterName,
        'class': _class,
        'itemLV': float(itemLV),
        'battleLV': int(battleLV),
        'expeditionLV': int(expeditionLV),
        'engraving_simple': engraving_simple,
        'engraving_detail': engraving_detail,
        'stat': stat,
        'card': card,
        'gem_simple': gem_simple,
        'equipment': equipment,
        'equipment_name': equipment_name,
        'accessory': accessory,
        'power': int(power),
        'vitality': int(vitality)
    }

    return character_data


def get_material_price():
    itemPriceDict = {}
    itemCodeList = [
        66102003,       # 파괴석 결정
        66102004,       # 파괴강석
        66102005,       # 정제된 파괴강석
        66102103,       # 수호석 결정
        66102104,       # 수호강석
        66102105,       # 정제된 수호강석
        66110221,       # 명예의 돌파석
        66110222,       # 위대한 명예의 돌파석
        66110223,       # 경이로운 명예의 돌파석
        66110224,       # 찬란한 명예의 돌파석
        6861007,        # 하급 오레하 융화 재료
        6861008,        # 중급 오레하 융화 재료
        6861009,        # 상급 오레하 융화 재료
        6861011,        # 최상급 오레하 융화 재료
        66130131,       # 명예의 파편 주머니(소)
        66130132,       # 명예의 파편 주머니(중)
        66130133,       # 명예의 파편 주머니(대)
    ]
    for itemCode in itemCodeList:
        url = "https://developer-lostark.game.onstove.com/markets/items/" + str(itemCode)
        itemData = lark_request('get', url)[0]
        itemName = itemData['Name']
        itemPrice = itemData['Stats'][0]['AvgPrice']
        print(f'{itemName}: {itemPrice}')
        itemPriceDict[itemName] = itemPrice

    return itemPriceDict


def get_gem_price():
    gemPriceDict = {}
    url = "https://developer-lostark.game.onstove.com/auctions/items"
    gemList = ["7레벨 멸", "7레벨 홍", "8레벨 멸", "8레벨 홍", "9레벨 멸", "9레벨 홍", "10레벨 멸", "10레벨 홍", ]
    for gemName in gemList:
        parameters = {
            "ItemLevelMin": 0,
            "ItemLevelMax": 1700,
            "Sort": "BUY_PRICE",
            "CategoryCode": 210000,
            "ItemTier": 3,
            "ItemName": gemName,
            "PageNo": 0,
            "SortCondition": "ASC"
        }
        itemData = lark_request('post', url, parameters)
        itemName = gemName.replace('레벨 ', '')
        itemPrice = itemData['Items'][0]['AuctionInfo']['BuyPrice']
        print(f'{itemName}: {itemPrice}')
        gemPriceDict[itemName] = itemPrice

    return gemPriceDict


def get_acc_price(accessory_data):
    url = "https://developer-lostark.game.onstove.com/auctions/items"
    accessory_data = accessory_data.split('/')
    accType = accessory_data[0]
    accGrade = accessory_data[1]
    accQuality = int(accessory_data[2])
    accEng1, accEng2 = accessory_data[3].split('_')
    accEng1_option, accEng1_value = accEng1.split('+')
    accEng2_option, accEng2_value = accEng2.split('+')
    accNature1 = accessory_data[4]
    accNature2 = accessory_data[5] if len(accessory_data) > 5 else ''
    parameters = {
        "ItemLevelMin": 0,
        "ItemLevelMax": 1700,
        "ItemGradeQuality": accQuality//10*10 if accQuality != 100 else 90,
        "EtcOptions": [
            {
                "FirstOption": 3,
                "SecondOption": auction_dict.engraving_list[accEng1_option],
                "MinValue": int(accEng1_value),
                "MaxValue": int(accEng1_value)
            },
            {
                "FirstOption": 3,
                "SecondOption": auction_dict.engraving_list[accEng2_option],
                "MinValue": int(accEng2_value),
                "MaxValue": int(accEng2_value)
            },
            {
                "FirstOption": 2,
                "SecondOption": auction_dict.nature_list[accNature1]
            },
            {
                "FirstOption": 2,
                "SecondOption": auction_dict.nature_list[accNature2]
            }
        ],
        "Sort": "BUY_PRICE",
        "CategoryCode": auction_dict.category[accType],
        "ItemTier": 3,
        "ItemGrade": accGrade,
        "PageNo": 0,
        "SortCondition": "ASC"
    }
    accPrice = 0
    itemData = lark_request('post', url, parameters)
    if itemData['Items']:
        accPrice = [item["AuctionInfo"]["BuyPrice"] for item in itemData['Items'] if item["AuctionInfo"]["BuyPrice"]][0]

    return accPrice


def gather_members(members):
    member_data_list = []
    global equipSetLevel
    equipSetLevel = load_yaml('./_data/equipment_set.yml')
    for member in members:
        member_data = get_characterInfo(member)
        if member_data:
            member_data_list.append(member_data)
            print(member, 'complete')
        else:
            print(member, 'fail')
    df_members = pd.DataFrame(data=member_data_list)
    df_members = df_members.sort_values(by='itemLV', ascending=False)

    return df_members


def capitalization(df_members):
    capitalization_data = []
    members = df_members.to_dict('records')
    step_price = pd.read_csv('./_data/step_price.csv').to_dict('records')
    gemPriceDict = pd.read_csv('./_data/material_price.csv', index_col=0).to_dict('records')[-1]
    df_baseAccDict = pd.read_csv('./_data/accessory_dict.csv', keep_default_na=False)

    for member in members:

        # equip
        i, equipTotal, equipPart = 0, 0, []
        equips = member['equipment'].split(',')
        for equip in equips:
            equipPrice = 0
            equipDetail = equip.split('/')
            equipStep = int(equipDetail[1])
            equipLevel = equipDetail[2].replace('lv', '')
            for step in step_price:
                step_level = step['level'].replace('level_', '')
                step_num = int(step['step'].replace('step_', ''))
                if step_level == equipLevel and step_num > equipStep: break
                if step_level == '1302' and step_num > 15: continue
                if step_level == '1340' and (step_num <= 6 or step_num > 20): continue
                if step_level == '1390' and (step_num <= 12 or step_num > 19): continue
                if step_level == '1525' and step_num <= 12: continue
                if i == 0:
                    equipPrice += step['weaponAvg']
                else:
                    equipPrice += step['armorAvg']
            equipTotal += equipPrice
            equipPart.append(equipPrice)
            i += 1

        # gem
        gemTotal, gemPart = 0, []
        gems = member['gem_simple'].split(',') if member['gem_simple'] == member['gem_simple'] and member['gem_simple'] else []
        for gem in gems:
            gemType,  gemCount = gem.split(' x')
            gemPrice = gemPriceDict[gemType] * int(gemCount) if gemType in gemPriceDict else 0
            gemTotal += gemPrice
            gemPart.append(gemPrice)

        # acc
        accTotal, accPart = 0, []
        accs = member['accessory'].split(',')
        for acc in accs:
            accData = split_accessory(acc)
            cd1 = df_baseAccDict['category'] == accData['accType']
            cd2 = df_baseAccDict['grade'] == accData['accGrade']
            cd3 = df_baseAccDict['quality'] == accData['accQuality']
            cd4 = df_baseAccDict['nature1'] == accData['accNature1']
            cd5 = df_baseAccDict['nature2'] == accData['accNature2']
            cd6 = df_baseAccDict['engraving1'] == accData['accEngraving1']
            cd7 = df_baseAccDict['engraving2'] == accData['accEngraving2']
            accPrice = df_baseAccDict[cd1 & cd2 & cd3 & cd4 & cd5 & cd6 & cd7]['price'].values
            if accPrice.size > 0:
                accPrice = accPrice[0]
            else:
                accPrice = 0
            accTotal += accPrice
            accPart.append(accPrice)

        gemPart = ','.join(map(str, gemPart))
        equipPart = ','.join(map(str, equipPart))
        accPart = ','.join(map(str, accPart))
        total = accTotal + gemTotal + equipTotal

        data = {
            'name': member['name'],
            'total': total,
            'accTotal': accTotal,
            'accPart': accPart,
            'gemTotal': gemTotal,
            'gemPart': gemPart,
            'equipTotal': equipTotal,
            'equipPart': equipPart,
        }
        capitalization_data.append(data)
        print(f'{data["name"]} accTotal:{data["accTotal"]} gemTotal:{data["gemTotal"]} equipTotal:{data["equipTotal"]}')
    df_capitalization = pd.DataFrame(data=capitalization_data)
    df_capitalization = df_capitalization.astype({'total': int, 'accTotal': int, 'gemTotal': int, 'equipTotal': int, 'accPart': str, 'gemPart': str, 'equipPart': str})
    df_capitalization = df_capitalization.sort_values(by='total', ascending=False)

    return df_capitalization


def get_news():
    url = "https://developer-lostark.game.onstove.com/news/events"
    response = requests.get(url, headers={"authorization": lark_api_key})
    if response.status_code == 200:
        news = json.loads(response.text)
    else:
        print("error")
        return

    df_news = pd.DataFrame(data=news)
    return df_news


def update_accdict(df_members, df_baseAccDict):
    accList = []
    for accs in df_members['accessory'].values.tolist():
        acc = accs.split(',')
        accList.extend(acc)

    KST = timezone(timedelta(days=-1, hours=9))
    date = datetime.now(KST).strftime('%y-%m-%d')
    accDict = []
    for acc in accList:
        accPrice = get_acc_price(acc)
        if accPrice == 0:
            print(f'{acc} 매물없음')
            print('---------------------------------')
            continue

        accessory_data = acc.split('/')
        accType = accessory_data[0]
        accGrade = accessory_data[1]
        accQuality = int(accessory_data[2])
        accQuality = accQuality//10*10 if accQuality != 100 else 90
        accEng1, accEng2 = accessory_data[3].split('_')
        accNature1 = accessory_data[4]
        accNature2 = accessory_data[5] if len(accessory_data) > 5 else ''
        accData = {
            'category': accType,
            'grade': accGrade,
            'quality': accQuality,
            'nature1': accNature1,
            'nature2': accNature2,
            'engraving1': accEng1,
            'engraving2': accEng2,
            'price': accPrice,
            'date': date
        }
        accDict.append(accData)
        print(accData)
        print('---------------------------------')
    df_accDict = pd.DataFrame(data=accDict)
    df_baseAccDict = df_baseAccDict.append(df_accDict)
    df_baseAccDict = df_baseAccDict.sort_values(by='date', ascending=False)
    df_baseAccDict = df_baseAccDict.drop_duplicates(['category', 'grade', 'quality', 'nature1', 'nature2', 'engraving1', 'engraving2'])
    df_baseAccDict = df_baseAccDict.astype({'category': str, 'grade': str, 'quality': int, 'nature1': str, 'nature2': str, 'engraving1': str, 'engraving2': str, 'price': str, 'date': str})
    df_baseAccDict = df_baseAccDict.sort_values(by=['grade', 'quality', 'nature2', 'category', 'nature1'], ascending=[True, False, False, True, False])

    return df_baseAccDict


# if __name__ == '__main__':
#     df_members = pd.read_csv('../_data/member_chart.csv')
#     update_accdict(df_members)


