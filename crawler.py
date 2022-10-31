import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime


def get_user_data(name):
    url = 'https://lostark.game.onstove.com/Profile/Character/'
    response = requests.get(url + name)
    soup = BeautifulSoup(response.text, 'html.parser')
    profile = soup.select_one('div.profile-ingame')
    if profile.select_one('div.profile-attention'):
        # print(f'{name} 캐럭터 정보가 없습니다')
        return

    _class = profile.select_one('div.profile-equipment__character > img')['alt']
    itemLV = profile.select('div.level-info2__expedition > span')[1].text.replace('Lv.', '').replace(',', '')
    battleLV = profile.select('div.level-info__item > span')[1].text.replace('Lv.', '')
    expeditionLV = profile.select('div.level-info__expedition > span')[1].text.replace('Lv.', '')

    engraving = [engraving.text for engraving in profile.select('div.profile-ability-engrave > div > div > ul > li > span')]
    engraving_detail = ','.join(engraving)
    engraving_simple = re.sub(r'[^0-9]', '', engraving_detail)

    stat = [stat.text for stat in profile.select('div.profile-ability-battle > ul > li > span')]
    stat = [f'{stat[i]} {stat[i + 1]}' for i in range(0, len(stat), 2) if stat[i] in ['치명', '특화', '신속']]
    stat = ','.join(stat)

    card = profile.select('div.profile-card__text > div > ul > li > div.card-effect__title')[-1].text
    card = ','.join(card.replace(')', '').split(' ('))

    gems = re.findall(r"\d{,2}레벨 ..(?=의 보석)", response.text)
    gems = sorted(gems, key=lambda x: (-int(re.search(r'\d+', x).group()), x.split()[1]))
    counter = {}
    for gem in gems:
        if gem in counter: counter[gem] += 1
        else: counter[gem] = 1
    gem_simple = ','.join(f'{key} x{value}' for key, value in counter.items())

    equipmentLV = re.findall(r"\+.+(?=</FONT></P>)", response.text)
    equipmentLV = ','.join(equipmentLV).replace('+', '')

    power = profile.select_one('div.profile-ability-basic > ul > li:nth-child(1) > span:nth-child(2)').text
    vitality = profile.select_one('div.profile-ability-basic > ul > li:nth-child(2) > span:nth-child(2)').text

    character_data = {
        'name': name,
        'class': _class,
        'itemLV': float(itemLV),
        'battleLV': int(battleLV),
        'expeditionLV': int(expeditionLV),
        'engraving_simple': engraving_simple,
        'engraving_detail': engraving_detail,
        'stat': stat,
        'card': card,
        'gem_simple': gem_simple,
        'equipmentLV': equipmentLV,
        'power': int(power),
        'vitality': int(vitality)
    }

    return character_data


def read_guild_members():
    f = open('./_data/guild_members.txt', 'r', encoding='UTF-8')
    members = f.read().split('\n')
    return members


def member_data_tocsv(guild_members):
    member_data_list = []
    for member in guild_members:
        member_data = get_user_data(member)
        if member_data:
            member_data_list.append(member_data)
            print(member, 'complete')
        else:
            print(member, 'fail')
    path = './_data/chart/' + datetime.now().strftime('%y-%m-%d') + '.csv'
    df_memberlist = pd.DataFrame(data=member_data_list)
    df_memberlist.sort_values(by=['itemLV'], ascending=False)
    df_memberlist.to_csv(path, index=False)


if __name__ == '__main__':
    guild_members = read_guild_members()
    member_data_tocsv(guild_members)
