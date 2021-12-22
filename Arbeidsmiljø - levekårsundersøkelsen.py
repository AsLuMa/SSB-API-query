from pyjstat import pyjstat
import requests
import matplotlib.pyplot as plt
import pandas as pd
import json

df_yh = pd.read_csv('yrkesrelaterte_helseplager.txt') #index_col=

print(df_yh.head(10).to_string())


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

# POST_URL_YRKESRELATERTE_HELSEPLAGER = 'https://data.ssb.no/api/v0/no/table/10478/'

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

def data_frå_API_til_dataframe(post_url, query):
  result = requests.post(post_url, json=query)
  pysjstat_dataset = pyjstat.Dataset.read(result.text)
  data_frame = pysjstat_dataset.write('dataframe')
  return data_frame

# def pretty_print():
#   string_of_data = ps_dataset
#   temp_string_for_prettyprint = json.loads(string_of_data)
#   print(json.dumps(temp_string_for_prettyprint, indent=4, sort_keys=True))


# Run once
df_yh = data_frå_API_til_dataframe('https://data.ssb.no/api/v0/no/table/10478/', yrkesrelaterte_helseplager)

# Data henta 22.12.21, klokka 21.07
df_yh.to_csv('yrkesrelaterte_helseplager.txt', index=False)
