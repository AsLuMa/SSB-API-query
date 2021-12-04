# ---- # GOALS

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
          "999A",
          "00-05",
          "06-15",
          "16-19",
          "20-29",
          "30-49",
          "50-66",
          "67-79",
          "80-89",
          "90+"
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

fastlege_query = {
  "query": [
    {
      "code": "Alder",
      "selection": {
        "filter": "item",
        "values": [
          "999A",
          "00-05",
          "06-15",
          "16-19",
          "20-29",
          "30-49",
          "50-66",
          "67-79",
          "80-89",
          "90+"
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

# INFO OM COLUMNS OG ROWS
# print(df_fastlege.columns.values)
# returns ['alder' 'kjønn' 'diagnose' 'statistikkvariabel' 'år' 'value']
# diagnose: Psykisk sykdom eller lidelse
# statistikkvariabel: Konsultasjoner per 1 000 innbyggere

# result_legevakt = requests.post(POST_URL_LEGEVAKT, json=legevakt_query)
result_fastlege = requests.post(POST_URL_FASTLEGE, json=fastlege_query)

# string_of_data = result_fastlege.text
# temp_string_for_prettyprint = json.loads(string_of_data)
# print(json.dumps(temp_string_for_prettyprint, indent=4, sort_keys=True))

#Pyjstat Dataset
# ds_legevakt = pyjstat.Dataset.read(result_legevakt.text)
ds_fastlege = pyjstat.Dataset.read(result_fastlege.text)

# Pandas DataFrame
# df_legevakt = ds_legevakt.write('dataframe')
df_fastlege = ds_fastlege.write('dataframe')


