import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from src.utils import load_yaml

def get_characterInfo(characterName):
    url = 'https://lostark.game.onstove.com/Profile/Character/'
    response = requests.get(url + characterName)
    soup = BeautifulSoup(response.text, 'html.parser')
    profile = soup.select_one('div.profile-ingame')
    if profile.select_one('div.profile-attention'):
        print(f'{characterName} 캐럭터 정보가 없습니다')
        return

    _class = profile.select_one('div.profile-equipment__character > img')['alt']
    itemLV = profile.select('div.level-info2__expedition > span')[1].text.replace('Lv.', '').replace(',', '')
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
    print(card)

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
            accType = typeValue.split()[-1]
            accQuality = equip['Element_001']['value']['qualityValue']
            accNature = '/'.join(re.sub('[^가-힣\s]', '', equip['Element_005']['value']['Element_001']).split())
            accEngraving = []
            for i in range(2):
                engraving = equip['Element_006']['value']['Element_000']['contentStr']['Element_00' + str(i)]['contentStr']
                engraving = ''.join(re.findall('(?<=>)[가-힣\s]+(?=<)|\+\d{1}', engraving))
                accEngraving.append(engraving)
            accEngraving = '_'.join(accEngraving)
            accessory.append(f'{accType}/{accQuality}/{accEngraving}/{accNature}')

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


if __name__ == '__main__':
    guild_members = load_yaml('../_data/guild_members.yml')
    guild_members = guild_members['main_character'] + guild_members['sub_character']

    df_members = gather_members(guild_members)

