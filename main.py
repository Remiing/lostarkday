import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime, timezone, timedelta
import yaml

from src.utils import load_yaml, classification, update_log
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
