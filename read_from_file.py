'''Data frå SSB henta 16.12.2021, klokka 19.36
Skript for å øve på databehandling frå fil, for å unngå mange queries til API-et'''

import pandas as pd
from pyjstat import pyjstat
import requests
import time
import json
import matplotlib.pyplot as plt

# ---- # Hente inn dataset frå fil
df_fastlege = pd.read_csv('temp_storage.txt')
# print(df_fastlege.to_string())


# ---- # Nokre print-statements for å sjå på data
# print(df_fastlege.kjønn)
# print(df_fastlege[90:110].to_string())

# ---- # Hente ut spesifikk rad, etter verdi frå kolonne
# print(df_fastlege.loc[df_fastlege['kjønn'] == 'Kvinner'].to_string())
# print(df_fastlege.loc[df_fastlege['alder'] == '30-49 år'].to_string())

# ---- # setter to kolonner som index
kjønn_og_alder_som_index = df_fastlege.set_index(['kjønn', 'alder']).sort_index(inplace=False)
# print(kjønn_og_alder_som_index.to_string())

# ---- # Henter bestemt kjønn og alder frå kolonne, basert på index satt over
print(kjønn_og_alder_som_index.loc['Menn', '16-19 år'].to_string())

# ---- # Ymse selects, projects og joins





# print(df_fastlege.isin(['Menn', 'kjønn']).to_string())



# matplotlib-stuff
