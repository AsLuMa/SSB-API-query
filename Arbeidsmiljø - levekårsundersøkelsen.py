from pyjstat import pyjstat
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json



# ---- # Kva vil eg ha av data?
# uavhnegig variabel: index = 'type helseproblem'
# statistisk signifikans mellom følgende uavhengige variabler:
# plot for:
  # ift den totale mengden sysselsatte - då må me hente ut det og lagre det i ein df (det kjem i rådata)
  # group by: 'kjønn'
  # group by: 'yrke'
  # group by 'år'

# ---- # Yrkesrelaterte helseplager
#index_col= to set index
df_yh = pd.read_csv('yrkesrelaterte_helseplager.txt', index_col='type helseproblem')

#'type helseproblem' - psykiske
utvalgte_helseproblem = [
'Har vansker med å sove fordi de tenker på jobb, ukentlig','Føler seg psykisk utmattet når de kommer hjem fra arbeid, ukentlig',
'Hodepine eller migrene som skyldes jobb',
'Plaget av angst som skyldes jobb',
'Plaget av depresjon eller kjenner seg nedtrykt som skyldes jobb',
'Tetthet i brystet, piping i brystet som skyldes jobb',
'Antall ansatte', 'Antall sysselsatte'
]

# print(df_yh.head(15).to_string())

# DataFrame
df_na_removed = df_yh.loc[utvalgte_helseproblem].dropna()
print(df_na_removed.to_string())





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




