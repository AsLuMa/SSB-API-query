# ---- #

import pandas as pd
from pyjstat import pyjstat
import requests
import time
import json
import matplotlib.pyplot as plt

time.sleep(4)

# 10903: Legevaktkonsultasjoner, etter år, statistikkvariabel, alder, diagnose og kjønn
POST_URL_LEGEVAKT = 'https://data.ssb.no/api/v0/no/table/10903/'
# 10141: Konsultasjoner hos fastlegen, etter år, statistikkvariabel, alder, diagnose og kjønn
POST_URL_FASTLEGE = 'https://data.ssb.no/api/v0/no/table/10141/'

legevakt_query = {
  "query": [
    {
      "code": "Alder",
      "selection": {
        "filter": "item",
        "values": [
          "999A" #,
          # "00-05",
          # "06-15",
          # "16-19",
          # "20-29",
          # "30-49",
          # "50-66",
          # "67-79",
          # "80-89",
          # "90+"
        ]
      }
    },
    {
      "code": "Kjonn",
      "selection": {
        "filter": "item",
        "values": [
          "0" #,
          # "1",
          # "2"
        ]
      }
    },
    {
      "code": "Diagnose2",
      "selection": {
        "filter": "vs:ICPC2a",
        "values": [
          "06"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "KonsultPerInnbygger"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

# Kommentert ut variablar, sånn at dette representerer alle kjønn og alle aldre
fastlege_query = {
  "query": [
    {
      "code": "Alder",
      "selection": {
        "filter": "item",
        "values": [
          "999A" #,
          # "00-05",
          # "06-15",
          # "16-19",
          # "20-29",
          # "30-49",
          # "50-66",
          # "67-79",
          # "80-89",
          # "90+"
        ]
      }
    },
    {
      "code": "Kjonn",
      "selection": {
        "filter": "item",
        "values": [
          "0" #,
          # "1",
          # "2"
        ]
      }
    },
    {
      "code": "Diagnose2",
      "selection": {
        "filter": "vs:ICPC2a",
        "values": [
          "06"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "KonsultPerInnbygger"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

result_legevakt = requests.post(POST_URL_LEGEVAKT, json=legevakt_query)
result_fastlege = requests.post(POST_URL_FASTLEGE, json=fastlege_query)

# string_of_data = result_fastlege.text
# temp_string_for_prettyprint = json.loads(string_of_data)
# print(json.dumps(temp_string_for_prettyprint, indent=4, sort_keys=True))

#Pyjstat Dataset: columns: ['alder' 'kjønn' 'diagnose' 'statistikkvariabel' 'år' 'value']
ds_legevakt = pyjstat.Dataset.read(result_legevakt.text)
ds_fastlege = pyjstat.Dataset.read(result_fastlege.text)

# Pandas DataFrame
df_legevakt = ds_legevakt.write('dataframe')
df_fastlege = ds_fastlege.write('dataframe')

'''Printer informasjon om DataFrame'''
# print(df_fastlege.to_string())
# print("index", df_fastlege.index)
# print("columns", df_fastlege.columns)
# print("values", df_fastlege.values)
# print(df_fastlege.dtypes)

'''Kjør denne når du vil ha oppdaterte data til temp_storage-filen. Sist oppdater 16.12.21'''
# df_fastlege.to_csv('temp_storage.txt', index=False)

konsultasjoner_fastlege = df_fastlege[df_fastlege['statistikkvariabel'] == 'Konsultasjoner per 1 000 innbyggere']
konsultasjoner_fastlege_indexed = df_fastlege.set_index('år')

konsultasjoner_legevakt = df_legevakt[df_legevakt['statistikkvariabel'] == 'Konsultasjoner per 1 000 innbyggere']
konsultasjoner_legevakt_indexed = df_legevakt.set_index('år')


def show_figure():
  # fig, ax = plt.subplots()
  plt.plot('år', 'value', data=df_fastlege)
  plt.plot('år', 'value', data=df_legevakt)
  plt.ylim(0, 1000)

  # konsultasjoner_fastlege_indexed.plot(ax=ax, y='value', label="Konsultasjoner hos fastlege: diagnose psykiske lidelser")
  # konsultasjoner_legevakt_indexed.plot(ax=ax, y='value', label="Konsultasjoner hos legevakt: diagnose psykiske lidelser")
  # ax.set_ylim(ymin=0, ymax=1000)
  plt.show()

show_figure()


