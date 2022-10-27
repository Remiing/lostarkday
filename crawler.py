import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def get_user_data(character_name):
    url = 'https://lostark.game.onstove.com/Profile/Character/'
    response = requests.get(url + character_name)
    soup = BeautifulSoup(response.text, 'html.parser')
    profile = soup.select_one('div.profile-ingame')
    if profile.select_one('div.profile-attention'):
        # print(f'{character_name} 캐럭터 정보가 없습니다')
        return

    character_class = profile.select_one('div.profile-equipment__character > img')['alt']

    character_item_level = profile.select('div.level-info2__expedition > span')[1].text.replace('Lv.', '').replace(',', '')

    character_battle_level = profile.select('div.level-info__item > span')[1].text.replace('Lv.', '')

    character_expedition_level = profile.select('div.level-info__expedition > span')[1].text.replace('Lv.', '')

    character_engraving = [engraving.text for engraving in profile.select('div.profile-ability-engrave > div > div > ul > li > span')]
    character_engraving = ','.join(character_engraving)

    character_stat = [stat.text for stat in profile.select('div.profile-ability-battle > ul > li > span')]
    character_stat = [f'{character_stat[i]} {character_stat[i + 1]}' for i in range(0, len(character_stat), 2) if character_stat[i] in ['치명', '특화', '신속']]
    character_stat = ','.join(character_stat)

    character_card = profile.select('div.profile-card__text > div > ul > li > div.card-effect__title')[-1].text

    character_gem = re.findall(r"\d{,2}레벨 ..의 보석", response.text)
    character_gem = sorted(character_gem, key=lambda x: (-int(re.search(r'\d+', x).group()), x.split()[1]))
    character_gem = ','.join(character_gem)

    character_equipment_level = re.findall(r"\+.+(?=</FONT></P>)", response.text)
    character_equipment_level = ','.join(character_equipment_level).replace('+', '')

    character_power = profile.select_one('div.profile-ability-basic > ul > li:nth-child(1) > span:nth-child(2)').text

    character_vitality = profile.select_one('div.profile-ability-basic > ul > li:nth-child(2) > span:nth-child(2)').text

    character_data = {
        'character_name': character_name,
        'character_class': character_class,
        'character_item_level': float(character_item_level),
        'character_battle_level': int(character_battle_level),
        'character_expedition_level': int(character_expedition_level),
        'character_engraving': character_engraving,
        'character_stat': character_stat,
        'character_card': character_card,
        'character_gem': character_gem,
        'character_equipment_level': character_equipment_level,
        'character_power': int(character_power),
        'character_vitality': int(character_vitality)
    }

    return character_data


def read_guild_members():
    f = open('./guild_members.txt', 'r', encoding='UTF-8')
    members = f.read().split('\n')
    return members


def member_data_tocsv(guild_members):
    member_data_list = []
    for member in guild_members:
        member_data = get_user_data(member)
        if member_data:
            member_data_list.append(member_data)
            # print(member, 'complete')
    df_memberlist = pd.DataFrame(data=member_data_list)
    df_memberlist.to_csv('./_data/memberlist.csv', index=False)


if __name__ == '__main__':
    guild_members = read_guild_members()
    member_data_tocsv(guild_members)
