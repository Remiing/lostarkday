import pandas as pd
from datetime import datetime, timezone, timedelta
import yaml
import os


def read_data():
    with open('./_data/guild_members.yml', encoding='utf-8') as file:
        members = yaml.load(file, Loader=yaml.FullLoader)
        members = members['main_character'] + members['sub_character']
    return members


def load_yaml(path):
    with open(path, encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def classification(df):
    level_list = df['itemLV'].to_list()
    representative_value = {
        'highest_level': int(level_list[0]),
        'average_level': int(sum(level_list)/len(level_list)),
        'lowest_level': int(level_list[-1])
    }
    variance = {
        'above_1620': 0,
        'above_1610': 0,
        'above_1600': 0,
        'above_1590': 0,
        'above_1580': 0,
        'above_1570': 0,
        'above_1560': 0,
        'above_1550': 0,
        'above_1540': 0,
        'above_1530': 0,
        'above_1520': 0,
        'above_1510': 0,
        'above_1500': 0,
        'above_1490': 0,
        'under_1490': 0,
    }
    for level in level_list:
        if level >= 1620: variance['above_1620'] += 1
        elif level >= 1610: variance['above_1610'] += 1
        elif level >= 1600: variance['above_1600'] += 1
        elif level >= 1590: variance['above_1590'] += 1
        elif level >= 1580: variance['above_1580'] += 1
        elif level >= 1570: variance['above_1570'] += 1
        elif level >= 1560: variance['above_1560'] += 1
        elif level >= 1550: variance['above_1550'] += 1
        elif level >= 1540: variance['above_1540'] += 1
        elif level >= 1530: variance['above_1530'] += 1
        elif level >= 1520: variance['above_1520'] += 1
        elif level >= 1510: variance['above_1510'] += 1
        elif level >= 1500: variance['above_1500'] += 1
        elif level >= 1490: variance['above_1490'] += 1
        else: variance['under_1490'] += 1

    class_list = df['class'].to_list()
    class_num = {}
    class_num['Berserker'] = class_list.count('버서커')
    class_num['Destroyer'] = class_list.count('디스트로이어')
    class_num['Gunlancer'] = class_list.count('워로드')
    class_num['Paladin'] = class_list.count('홀리나이트')
    class_num['Arcanist'] = class_list.count('아르카나')
    class_num['Summoner'] = class_list.count('서머너')
    class_num['Bard'] = class_list.count('바드')
    class_num['Sorceress'] = class_list.count('소서리스')
    class_num['Wardancer'] = class_list.count('배틀마스터')
    class_num['Scrapper'] = class_list.count('인파이터')
    class_num['Soulfist'] = class_list.count('기공사')
    class_num['Glaivier'] = class_list.count('창술사')
    class_num['Striker'] = class_list.count('스트라이커')
    class_num['Deathblade'] = class_list.count('블레이드')
    class_num['Shadowhunter'] = class_list.count('데모닉')
    class_num['Reaper'] = class_list.count('리퍼')
    class_num['Sharpshooter'] = class_list.count('호크아이')
    class_num['Deadeye'] = class_list.count('데빌헌터')
    class_num['Artillerist'] = class_list.count('블래스터')
    class_num['Machinist'] = class_list.count('스카우터')
    class_num['Gunslinger'] = class_list.count('건슬링어')
    class_num['Artist'] = class_list.count('도화가')
    class_num['Aeromancer'] = class_list.count('기상술사')

    data = {'representative_value': representative_value,
            'variance': variance,
            'class_num': class_num
            }
    return data


def update_log(filename):
    KST = timezone(timedelta(hours=9))
    update_time = datetime.now(KST).strftime('%y-%m-%d %H:%M:%S')
    log = {
        'filename': filename,
        'update_time': update_time
    }
    return [log]


def modify_data():
    equipSetLevel = load_yaml('../_data/equipment_set.yml')
    basepath = '../_data/chart/'
    filelist = os.listdir(basepath)
    print(filelist)

    for file in filelist[:]:
        print(file)
        df = pd.read_csv(basepath + file)
        df = df.to_dict('records')
        datalist = []
        for data in df:
            equip = data['equipmentLV'].split(',')
            equipment, equipment_name = [], []
            for i in equip:
                equipType = i.split()[-1]
                equipStep = i[0:i.find(' ')]
                equipName = i[i.find(' ') + 1:]
                equipQuality = 0
                equipLevel = ''
                for k, v in equipSetLevel.items():
                    for setName in v:
                        if setName in equipName:
                            equipLevel = k
                            break
                    else:
                        continue
                    break
                equipment.append(f'{equipType}/{equipStep}/{equipLevel}/{equipQuality}')
                equipment_name.append(equipName)
            equipment = ','.join(equipment)
            equipment_name = ','.join(equipment_name)
            character_data = {
                'name': data['name'],
                'class': data['class'],
                'itemLV': data['itemLV'],
                'battleLV': data['battleLV'],
                'expeditionLV': data['expeditionLV'],
                'engraving_simple': data['engraving_simple'],
                'engraving_detail': data['engraving_detail'],
                'stat': data['stat'],
                'card': data['card'],
                'gem_simple': data['gem_simple'].replace('레벨 ', '').replace('염', '').replace('화', '') if data['gem_simple'] == data['gem_simple'] else '',
                'equipment': equipment,
                'equipment_name': equipment_name,
                'accessory': '',
                'power': data['power'],
                'vitality': data['vitality']
            }
            print(character_data)
            datalist.append(character_data)

        df_members = pd.DataFrame(data=datalist)
        df_members.to_csv(basepath + file, index=False)


if __name__ == '__main__':
    modify_data()
