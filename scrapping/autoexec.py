from scrapping import http, base, metropole_stations
import shutil
from os.path import exists
import os
import pandas as pd
import re

class Autoexec:
    
    def auto_download(self):
        for year in range(1996,2024):
            for month in range(1,13):
                filename = "../data/%d-%02d.csv.gz" % (year, month)
                if not exists(filename):
                    with http.request(
                         'GET',base+'synop.%d%02d.csv.gz'% (year,month),
                        preload_content=False) as r,\
                        open(filename, 'wb') as out_file:
                        shutil.copyfileobj(r, out_file)
    def make_data(self):
        reg = re.compile(r'^\d{4}-\d{2}\.csv.gz')
        dfs = []
        metropole = metropole_stations()
        for file in filter(reg.search, os.listdir('../data')):
            data = pd.read_csv(f'../data/{file}', delimiter=';',
                    parse_dates=['date'], na_values=['mq'])
            dfs.append(data[data.numer_sta.isin(metropole)])
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv("Report/data/france.csv.gz", sep=";", index=False)