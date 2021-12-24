from pyjstat import pyjstat
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json



# ---- # Kva vil eg ha av data?
# totale mengden sysselsatte + antall ansatte?

# statistisk signifikans: kvinner og menn?

# ---- # Yrkesrelaterte helseplager
df_yh = pd.read_csv('yrkesrelaterte_helseplager.txt', index_col='type helseproblem')

#'type helseproblem' - psykiske
utvalgte_helseproblem = [
'Har vansker med å sove fordi de tenker på jobb, ukentlig','Føler seg psykisk utmattet når de kommer hjem fra arbeid, ukentlig',
'Hodepine eller migrene som skyldes jobb',
'Plaget av angst som skyldes jobb',
'Plaget av depresjon eller kjenner seg nedtrykt som skyldes jobb',
'Tetthet i brystet, piping i brystet som skyldes jobb' #,
#'Antall ansatte', 'Antall sysselsatte'
]

# ---- # Løsning 2

df_ny = df_yh.loc[(df_yh['yrke'] == 'Alle yrker') & (df_yh['år'] == 2019)]
df = df_ny.loc[utvalgte_helseproblem].dropna()

group_kjønn = df.groupby('kjønn')
df_menn = group_kjønn.get_group('Menn')['value']
df_kvinner = group_kjønn.get_group('Kvinner')['value']
df_begge = group_kjønn.get_group('Begge kjønn')['value']

# --- # Bar chart
y_indexes = np.arange(len(df_begge))
width = 0.25

plt.style.use('seaborn')
plt.title(f"Yrkesrelaterte helseplager")
# - width shifts to left
plt.bar(y_indexes - width, df_menn, width=width, label="Menn")
plt.bar(y_indexes, df_kvinner, width=width, label="Kvinner")
# + width shifts to right
plt.bar(y_indexes + width, df_begge, width=width, label="Begge kjønn")

short_labels = ['Utmattet', 'Hodepine', 'Angst', 'Depresjon', 'Tetthet i brystet']
plt.xticks(ticks=y_indexes, labels=short_labels)
# print(df_menn.index)
# df_menn.index

plt.xlabel("")
plt.ylabel("")
# plt.ylim(0, 1000)
plt.legend()
plt.show()



# ---- # Løsning 1 - litt uelegant

# DataFrame TODO mangler yrke og type helseproblem
# df_utvalgte = df_yh.loc[utvalgte_helseproblem]
# df_indexåy = df_utvalgte.set_index(['yrke', 'år'])
# df_yrke = df_indexåy.loc['Alle yrker']
# df_år = df_yrke.loc[2019]
# print(df_år)





exit()


# ---- # Arbeidmiljø, levekårsundersøkelsen
# 10478: Yrkesrelaterte helseplager, arbeidsulykker og sykefravær for sysselsatte, etter yrke (1-siffernivå) og kjønn (prosent) 2013 - 2019
# https://www.ssb.no/statbank/table/10478

####
# 07991: Tilknytning til arbeidsplassen og ulike arbeidsforhold, etter kjønn og næring (SN2007) (prosent) 2009 - 2019
# https://www.ssb.no/statbank/table/07991

# 10477: Psykososialt arbeidsmiljø. Hjelp og tilbakemelding, samarbeid, verdsetting, vold og trakassering, etter yrke (2-siffernivå) (prosent) 2013 - 2019
# https://www.ssb.no/statbank/table/10477

# 10481: Jobbkrav, kontroll, rollekonflikt og forventning i jobben, etter yrke (2-siffernivå) (prosent) 2013 - 2019
# https://www.ssb.no/statbank/table/10481

#### Skript for å hente ut info frå SSB, skrive til DataFrame og lagre som CSV

yrkesrelaterte_helseplager = {
  "query": [
    {
      "code": "NYK",
      "selection": {
        "filter": "item",
        "values": [
          "0-9",
          "1",
          "2+35",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "0+3351+3355+54"
        ]
      }
    },
    {
      "code": "Kjonn",
      "selection": {
        "filter": "item",
        "values": [
          "0",
          "1",
          "2"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}


# noinspection NonAsciiCharacters
def data_frå_API_til_dataframe(post_url, query):
  result = requests.post(post_url, json=query)
  pysjstat_dataset = pyjstat.Dataset.read(result.text)
  data_frame = pysjstat_dataset.write('dataframe')
  return data_frame

# # Run once
# df_yh = data_frå_API_til_dataframe('https://data.ssb.no/api/v0/no/table/10478/', yrkesrelaterte_helseplager)
#
# # Data henta 22.12.21, klokka 21.07
# df_yh.to_csv('yrkesrelaterte_helseplager.txt', index=False)




