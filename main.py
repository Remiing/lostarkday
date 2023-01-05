import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime, timezone, timedelta
import yaml

from src.utils import load_yaml, classification, update_log, calcStepPrice
from src import crawling


if __name__ == '__main__':
    guild_members = load_yaml('./_data/guild_members.yml')
    guild_members = guild_members['main_character'] + guild_members['sub_character']

    df_members = crawling.gather_members(guild_members)

    path = './_data/chart/'
    KST = timezone(timedelta(days=-1, hours=9))
    filename = datetime.now(KST).strftime('%y-%m-%d') + '.csv'
    df_members.to_csv(path + filename, index=False)
    df_members.to_csv('./_data/member_chart.csv', index=False)

    classification_data = classification(df_members)
    with open('./_data/total_info.yml', 'w') as file:
        yaml.dump(classification_data, file, default_flow_style=False)
    log = update_log(filename)
    with open('./_data/update_time.yml', 'a') as file:
        yaml.dump(log, file, default_flow_style=False)

    df_itemPrice = crawling.get_material_price()
    df_gemPrice = crawling.get_gem_price()
    df_materialPrice = pd.concat((df_itemPrice, df_gemPrice), sort=False)
    df_materialPrice.to_csv('./_data/material_price.csv', index=False)

    df_stepPrice = calcStepPrice()
    df_stepPrice.to_csv('./_data/step_price.csv', index=False)
    
    df_members = pd.read_csv('./_data/member_chart.csv')
    df_capitalization = crawling.capitalization(df_members)
    df_capitalization.to_csv('./_data/capitalization.csv', index=False)

