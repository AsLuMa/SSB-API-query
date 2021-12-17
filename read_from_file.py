'''Data frå SSB henta 16.12.2021, klokka 19.36
Skript for å øve på databehandling frå fil, for å unngå mange queries til API-et'''

import pandas as pd
from pyjstat import pyjstat
import requests
import time
import json
import matplotlib.pyplot as plt

# ---- # Hente inn dataset frå fil
df_fastlege = pd.read_csv('temp_storage.txt', index_col=['alder', 'kjønn'])


# variabler til graf i matplotlib: y-akse
kjønn_group = df_fastlege.groupby(['kjønn'])
menn_alle_aldre = kjønn_group.get_group('Menn').loc['Alle aldre']['value']
kvinner_alle_aldre = kjønn_group.get_group('Kvinner').loc['Alle aldre']['value']
begge_kjønn_alle_aldre = kjønn_group.get_group('Begge kjønn').loc['Alle aldre']['value']

# variabler til x-akse
år = kjønn_group.get_group('Begge kjønn').loc['Alle aldre']['år']

### Graf i matplotlib
plt.title(f"Konsultasjoner hos fastlege for psykiske lidelser")
plt.plot(år, kvinner_alle_aldre, label = "Kvinner")
plt.plot(år, menn_alle_aldre, label = "Menn")
plt.plot(år, begge_kjønn_alle_aldre, marker='.', label = "Begge kjønn")
plt.xlabel("År")
plt.ylabel("Konsultasjoner per 1000")
plt.ylim(0, 1000)
plt.legend()
plt.show()





# ---- # NOTATER
# ---- # Nokre print-statements for å sjå på data
# print(df_fastlege.kjønn)
# print(df_fastlege[90:110].to_string())

# ---- # Hente ut spesifikk rad, etter verdi frå kolonne, returns series-object with true-false values
# print(df_fastlege.loc[df_fastlege['kjønn'] == 'Kvinner'].to_string())
# print(df_fastlege.loc[df_fastlege['alder'] == '30-49 år'].to_string())

# ---- # setter to kolonner som index, inplace=True endrer det originale datasettet
# kjønn_og_alder_som_index = df_fastlege.set_index(['kjønn', 'alder']).sort_index(inplace=False)
# print(kjønn_og_alder_som_index.to_string())


# ---- # Ymse selects, projects og joins
# Henter bestemt kjønn og alder frå kolonne, basert på index satt over
# print(kjønn_og_alder_som_index.loc['Menn', '16-19 år'].to_string())

# search ['row', ['column1', 'column2']]
# print(kjønn_og_alder_som_index.loc['Kvinner', ['år', 'value']][0:20].to_string())

# filtering - sammenligne rader, hente kolonner, kan ikke bruke built-in comparison operators, tenk Java-operators, ~for å negate filter
# filter return series of true-false values - returns only true values
# TODO skifte index til kjønn for å slippe å få med index-rada
# filter_kjønn_kvinner = (df_fastlege['kjønn'] == 'Kvinner') & (df_fastlege['alder'] == '0-5 år')
# ting = df_fastlege.loc[filter_kjønn_kvinner, ['alder', 'år', 'value']]
# print(ting.to_string()) # DataFrame-type

# print(df_fastlege.isin(['Menn', 'kjønn']).to_string()) # kan òg passe inn liste med kolonne-labels her
# str.contains('str', na=False)

# --- # SORTING
# df_fastlege.sort_values(by='column')
# df_fastlege.sort_values(by=['list of', 'columns'], ascending=[False, True])

# --- # Grouping and aggregating data
# print(df_fastlege['alder'].value_counts() #gir liten meining med akkurat dette datasettet
# group_by: split, apply function, combine result

# print(menn_alle_aldre)
# print(kvinner_alle_aldre)
# print(begge_kjønn_alle_aldre)
# print(år)



# print(menn_alle_aldre.to_string())
# print(kvinner_alle_aldre.to_string())

# år_group = df_fastlege.groupby(['år'])
# print(år_group.get_group(2015).to_string())

# combine series with concat([series1, series2], axis = 'columns') #axis here is what you concat on, default is row
# rename column names so they better fit the concatenated data





















