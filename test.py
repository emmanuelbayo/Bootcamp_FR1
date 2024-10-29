import pandas as pd 
import re
import os
from scrapping import metropole_stations
reg = re.compile(r'^\d{4}-\d{2}\.csv.gz')
dfs = []
metropole = metropole_stations()
for file in filter(reg.search, os.listdir('scrapping/data')):
    data = pd.read_csv(f'scrapping/data/{file}', delimiter=';',
            parse_dates=['date'], na_values=['mq'],compression='gzip', encoding='utf-8')
    dfs.append(data[data.numer_sta.isin(metropole)])
df = pd.concat(dfs, ignore_index=True)


print(df.head())

print(df.head())