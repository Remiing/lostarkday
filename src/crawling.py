import os
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from src.utils import load_yaml
from dotenv import load_dotenv
from src import auction_dict

load_dotenv()
lark_api_key = 'bearer ' + os.environ.get('lark_api_key')


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
        response = requests.get(url, headers={"authorization": lark_api_key})
        if response.status_code == 200:
            itemData = json.loads(response.text)[0]
            itemName = itemData['Name']
            itemPrice = itemData['Stats'][0]['AvgPrice']
            print(f'{itemName}: {itemPrice}')
            itemPriceDict[itemName] = itemPrice
        else:
            print("error")

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
        response = requests.post(url, headers={"authorization": lark_api_key}, json=parameters)
        if response.status_code == 200:
            itemData = json.loads(response.text)
            itemName = gemName.replace('레벨 ', '')
            itemPrice = itemData['Items'][0]['AuctionInfo']['BuyPrice']
            print(f'{itemName}: {itemPrice}')
            gemPriceDict[itemName] = itemPrice
        else:
            print("error")
            break

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
    while True:
        response = requests.post(url, headers={"authorization": lark_api_key}, json=parameters)
        if response.status_code != 200:
            if 'retry-after' in response.headers:
                time.sleep(int(response.headers['retry-after'])+1)
                continue
            print('error')
            accPrice = -1
            break
        elif 'x-ratelimit-remaining' not in response.headers:
            continue
        else:
            accData = json.loads(response.text)
            if accData['Items']:
                accPrice = [item["AuctionInfo"]["BuyPrice"] for item in accData['Items'] if item["AuctionInfo"]["BuyPrice"]][0]
            break

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
    step_price = pd.read_csv('./_data/step_price.csv')
    step_price = step_price.to_dict('records')
    df_itemPrice = pd.read_csv('./_data/material_price.csv')
    gem_dict = {}
    for gemType, gemPrice in zip(list(df_itemPrice['itemName']), list(df_itemPrice['itemPrice'])):
        if '멸' in gemType or '홍' in gemType:
            gem_dict[gemType] = int(gemPrice)

    for member in members:
        print(member)

        # equip
        i, equipTotal, equipDetail = 0, 0, []
        equips = member['equipment'].split(',')
        for equip in equips:
            equipPrice = 0
            equipPart = equip.split('/')
            if i == 0: equipType = "무기"
            elif i == 1: equipType = "투구"
            elif i == 2: equipType = "상의"
            elif i == 3: equipType = "하의"
            elif i == 4: equipType = "장갑"
            else: equipType = "어깨"
            equipStep = int(equipPart[1])
            equipLevel = equipPart[2].replace('lv', '')
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
            equipDetail.append(f'{equipType} {equipStep} {equipPrice}')
            i += 1

        # gem
        gemTotal, gemDetail = 0, []
        gems = member['gem_simple'].split(',') if member['gem_simple'] == member['gem_simple'] and member['gem_simple'] else []
        for gem in gems:
            gemPart = gem.split(' x')
            gemType = gemPart[0]
            gemCount = int(gemPart[1])
            gemPrice = gem_dict[gemType] * gemCount if gemType in gem_dict else 0
            gemTotal += gemPrice
            gemDetail.append(f'{gem} {gemPrice}')

        # acc
        accTotal, accDetail = 0, []
        accs = member['accessory'].split(',')
        for acc in accs:
            accPrice = get_acc_price(acc)
            accTotal += accPrice
            accDetail.append(f'{acc} {accPrice}')

        gemDetail = ','.join(gemDetail)
        equipDetail = ','.join(equipDetail)
        accDetail = ','.join(accDetail)
        data = {
            'name': member['name'],
            'itemLV': member['itemLV'],
            'accTotal': accTotal,
            'accDetail': accDetail,
            'gemTotal': gemTotal,
            'gemDetail': gemDetail,
            'equipTotal': equipTotal,
            'equipDetail': equipDetail,
        }
        capitalization_data.append(data)
        print(f'{data["name"]} accTotal:{data["accTotal"]} gemTotal:{data["gemTotal"]} equipTotal:{data["equipTotal"]}')
    df_capitalization = pd.DataFrame(data=capitalization_data)

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


# if __name__ == '__main__':
    # guild_members = load_yaml('../_data/guild_members.yml')
    # guild_members = guild_members['main_character'] + guild_members['sub_character']
    #
    # df_members = gather_members(guild_members)
    #
    # itemPriceDict = get_material_price()
    # gemPriceDict = get_gem_price()

    # df_materialPrice = pd.concat((df_itemPrice, df_gemPrice), sort=False)
    # get_acc_price('귀걸이/고대/71/예리한 둔기+5_아드레날린+3/신속')
    # get_news()



