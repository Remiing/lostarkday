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
    class_num['Berserker'] = class_list.count('?????????')
    class_num['Destroyer'] = class_list.count('??????????????????')
    class_num['Gunlancer'] = class_list.count('?????????')
    class_num['Paladin'] = class_list.count('???????????????')
    class_num['Arcanist'] = class_list.count('????????????')
    class_num['Summoner'] = class_list.count('?????????')
    class_num['Bard'] = class_list.count('??????')
    class_num['Sorceress'] = class_list.count('????????????')
    class_num['Wardancer'] = class_list.count('???????????????')
    class_num['Scrapper'] = class_list.count('????????????')
    class_num['Soulfist'] = class_list.count('?????????')
    class_num['Glaivier'] = class_list.count('?????????')
    class_num['Striker'] = class_list.count('???????????????')
    class_num['Deathblade'] = class_list.count('????????????')
    class_num['Shadowhunter'] = class_list.count('?????????')
    class_num['Reaper'] = class_list.count('??????')
    class_num['Sharpshooter'] = class_list.count('????????????')
    class_num['Deadeye'] = class_list.count('????????????')
    class_num['Artillerist'] = class_list.count('????????????')
    class_num['Machinist'] = class_list.count('????????????')
    class_num['Gunslinger'] = class_list.count('????????????')
    class_num['Artist'] = class_list.count('?????????')
    class_num['Aeromancer'] = class_list.count('????????????')

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


def calcStepPrice():
    stepPrice = []

    df_itemPrice = pd.read_csv('./_data/material_price.csv')
    df_avg = pd.read_csv('./_data/avg_try_num.csv')
    df_weapon_step = pd.read_csv('./_data/material/weapon_step.csv')
    df_armor_step = pd.read_csv('./_data/material/armor_step.csv')

    honor_shard_list = list(df_itemPrice[df_itemPrice['itemName'].str.contains('????????? ?????? ?????????')]['itemPrice'])
    honor_shard_price = round((honor_shard_list[0] / 500 + honor_shard_list[1] / 1000 + honor_shard_list[2] / 1500) / 3, 2)

    for weapon_step, armor_step in zip(df_weapon_step.to_dict('records'), df_armor_step.to_dict('records')):
        destruction_stone_price, guardian_stone_price, leap_stone_price, fusion_price = 0, 0, 0, 0
        if weapon_step['level'] == 'level_1302':
            destruction_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ??????']['itemPrice'].values[0] / 10
            guardian_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ??????']['itemPrice'].values[0] / 10
            leap_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ?????????']['itemPrice'].values[0]
            fusion_price = df_itemPrice[df_itemPrice['itemName'] == '?????? ????????? ?????? ??????']['itemPrice'].values[0]
        elif weapon_step['level'] == 'level_1340':
            destruction_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ??????']['itemPrice'].values[0] / 10
            guardian_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ??????']['itemPrice'].values[0] / 10
            leap_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ????????? ?????????']['itemPrice'].values[0]
            fusion_price = df_itemPrice[df_itemPrice['itemName'] == '?????? ????????? ?????? ??????']['itemPrice'].values[0]
        elif weapon_step['level'] == 'level_1390':
            destruction_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????????']['itemPrice'].values[0] / 10
            guardian_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????????']['itemPrice'].values[0] / 10
            leap_stone_price = df_itemPrice[df_itemPrice['itemName'] == '???????????? ????????? ?????????']['itemPrice'].values[0]
            fusion_price = df_itemPrice[df_itemPrice['itemName'] == '?????? ????????? ?????? ??????']['itemPrice'].values[0]
        elif weapon_step['level'] == 'level_1525':
            destruction_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ????????????']['itemPrice'].values[0] / 10
            guardian_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ????????????']['itemPrice'].values[0] / 10
            leap_stone_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ????????? ?????????']['itemPrice'].values[0]
            fusion_price = df_itemPrice[df_itemPrice['itemName'] == '????????? ????????? ?????? ??????']['itemPrice'].values[0]

        prabability_data = df_avg[df_avg['probability'] == weapon_step['probability']].to_dict('records')[0]

        weapon_refining_once = round(weapon_step['destruction_stone'] * destruction_stone_price + weapon_step['leap_stone'] * leap_stone_price + weapon_step['fusion'] * fusion_price + weapon_step['honor_shard'] * honor_shard_price + weapon_step['gold'])
        weapon_refining_avg = round(weapon_refining_once * prabability_data['avg_num'])
        weapon_refining_max = round(weapon_refining_once * prabability_data['max_num'])
        armor_refining_once = round(armor_step['guardian_stone'] * guardian_stone_price + armor_step['leap_stone'] * leap_stone_price + armor_step['fusion'] * fusion_price + armor_step['honor_shard'] * honor_shard_price + armor_step['gold'])
        armor_refining_avg = round(armor_refining_once * prabability_data['avg_num'])
        armor_refining_max = round(armor_refining_once * prabability_data['max_num'])

        data = {'level': weapon_step['level'],
                'step': weapon_step['step'],
                'weaponOnce': int(weapon_refining_once),
                'weaponAvg': int(weapon_refining_avg),
                'weaponMax': int(weapon_refining_max),
                'armorOnce': int(armor_refining_once),
                'armorAvg': int(armor_refining_avg),
                'armorMax': int(armor_refining_max),
                }

        stepPrice.append(data)

    df_stepPrice = pd.DataFrame(data=stepPrice)
    df_stepPrice = df_stepPrice.astype({'weaponOnce': int, 'weaponAvg': int, 'weaponMax': int, 'armorOnce': int, 'armorAvg': int, 'armorMax': int, })

    return df_stepPrice


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
                'gem_simple': data['gem_simple'].replace('?????? ', '').replace('???', '').replace('???', '') if data['gem_simple'] == data['gem_simple'] else '',
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

