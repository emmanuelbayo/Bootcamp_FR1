import urllib3
import pandas as pd

http = urllib3.PoolManager()
base = 'https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/'

def metropole_stations():
    stations = pd.read_csv('Report/postesSynop.txt',sep=";")
    metropole = stations.ID[(stations.Latitude > 40) & (stations.Longitude > -10)]
    return metropole

