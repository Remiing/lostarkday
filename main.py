import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime, timezone, timedelta
import yaml

from src.utils import load_yaml, classification, update_log, calcStepPrice
from src import crawling


def runtest():
    guild_members = load_yaml('./_data/guild_members.yml')
    guild_members = guild_members['main_character'] + guild_members['sub_character']

    df_members = crawling.gather_members(guild_members)

    path = './test/chart/'
    KST = timezone(timedelta(days=-1, hours=9))
    date = datetime.now(KST).strftime('%y-%m-%d')
    filename = date + '.csv'
    df_members.to_csv(path + filename, index=False)
    df_members.to_csv('./test/member_chart.csv', index=False)

    classification_data = classification(df_members)
    with open('./test/total_info.yml', 'w') as file:
        yaml.dump(classification_data, file, default_flow_style=False)
    log = update_log(filename)
    with open('./test/update_time.yml', 'a') as file:
        yaml.dump(log, file, default_flow_style=False)

    itemPriceDict = crawling.get_material_price()
    gemPriceDict = crawling.get_gem_price()
    priceDict = dict(itemPriceDict, **gemPriceDict)
    df_todayMaterialPrice = pd.DataFrame(priceDict, index=[date])
    df_materialPrice = pd.read_csv('./test/material_price.csv', index_col=0)
    df_materialPrice = df_materialPrice.append(df_todayMaterialPrice)
    df_materialPrice.to_csv('./test/material_price.csv')

    df_stepPrice = calcStepPrice()
    df_stepPrice.to_csv('./test/step_price.csv', index=False)

    # df_capitalization = crawling.capitalization(df_members)
    # df_capitalization.to_csv('./test/capitalization.csv', index=False)
    #
    # df_news = crawling.get_news()
    # df_news.to_csv('./test/news.csv', index=False)

    df_accDict = crawling.update_accdict(df_members)
    df_accDict.to_csv('./test/accessory_dict.csv', index=False)


def run():
    guild_members = load_yaml('./_data/guild_members.yml')
    guild_members = guild_members['main_character'] + guild_members['sub_character']

    df_members = crawling.gather_members(guild_members)

    path = './_data/chart/'
    KST = timezone(timedelta(days=-1, hours=9))
    date = datetime.now(KST).strftime('%y-%m-%d')
    filename = date + '.csv'
    df_members.to_csv(path + filename, index=False)
    df_members.to_csv('./_data/member_chart.csv', index=False)

    classification_data = classification(df_members)
    with open('./_data/total_info.yml', 'w') as file:
        yaml.dump(classification_data, file, default_flow_style=False)
    log = update_log(filename)
    with open('./_data/update_time.yml', 'a') as file:
        yaml.dump(log, file, default_flow_style=False)

    itemPriceDict = crawling.get_material_price()
    gemPriceDict = crawling.get_gem_price()
    priceDict = dict(itemPriceDict, **gemPriceDict)
    df_todayMaterialPrice = pd.DataFrame(priceDict, index=[date])
    df_materialPrice = pd.read_csv('./_data/material_price.csv', index_col=0)
    df_materialPrice = df_materialPrice.append(df_todayMaterialPrice)
    df_materialPrice.to_csv('./_data/material_price.csv')

    df_stepPrice = calcStepPrice()
    df_stepPrice.to_csv('./_data/step_price.csv', index=False)

    # df_capitalization = crawling.capitalization(df_members)
    # df_capitalization.to_csv('./_data/capitalization.csv', index=False)

    # df_news = crawling.get_news()
    # df_news.to_csv('./_data/news.csv', index=False)

    df_accDict = crawling.update_accdict(df_members)
    df_accDict.to_csv('./_data/accessory_dict.csv', index=False)


if __name__ == '__main__':
    # runtest()
    run()

