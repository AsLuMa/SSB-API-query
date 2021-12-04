'''
Practice script to fetch and process information from Statistisk Sentralbyrå (SSB), using their API
https://www.ssb.no/api
Data fetched from table 04511: Psykisk helsevern for voksne. Døgnplasser, utskrivninger, oppholdsdøgn, polikliniske konsultasjoner og oppholdsdager, etter helseforetak 1990 - 2020
https://www.ssb.no/statbank/table/04511/
Kodeeksempel frå SSB: https://www.ssb.no/omssb/tjenester-og-verktoy/api/px-api/eksempler-pa-kode
R also has support for JSON-stat
'''

# API-console to autogenerate JSON-stat queries
# https://data.ssb.no/api/v0/no/console

### List of data to fetch/goals for script:
# Trender frå 1990-2020 i
# - døgnplasser
# - oppholdsdager
# - polikliniske konsultasjoner

# for alle regioner
# for HELSEREGION VEST TOTALT
# Avtalespesialiser i Helseregion Vest

# Graphics

# Statistikk
# - deskriptiv statistikk av HELSEREGION VEST TOTALT vs alle regioner
# - enkel t-test for HELSEREGION VEST TOTALT vs alle regioner

from pyjstat import pyjstat
import requests
import time
import json
import matplotlib.pyplot as plt

time.sleep(2)

#string
POST_URL = 'https://data.ssb.no/api/v0/no/table/04511'

# Helseregion Vest, tre siste år
# Dobbeltsjekk query mot https://www.ssb.no/statbank/table/04511/ - konsoll gav feil variabelnamn på polikliniske konsultasjonar
helseregion_vest_totalt_query = {
  "query": [
    {
      "code": "HelseReg",
      "selection": {
        "filter": "item",
        "values": [
          "H03_F"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "DPlasser",
          "Oppholdsdogn",
          "PolikliniskeKonsult"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "top",
        "values": [
          "3"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

# type = <class 'requests.models.Response'>
response = requests.post(POST_URL, json=helseregion_vest_totalt_query)
# print(response)

# dict to str, in order to pretty print the metadata we query
# streng_HR = str(helseregion_vest_totalt_query)
# print(json.dumps(helseregion_vest_totalt_query, indent=4, sort_keys=True))


# string_of_data = response.text
# # correct encoding of norwegian letters
# # print(string_of_data)
# #data as one long string, no longer correct encoding of norwegian letters TODO how to de-and encode as utf-8?
# temp_string_for_prettyprint = json.loads(string_of_data)
# # pretty printing of actual data
# print(json.dumps(temp_string_for_prettyprint, indent=4, sort_keys=True))

# return Pandas dataframe (what can I do with this?)
#  type = <class 'pyjstat.pyjstat.Dataset'>
dataset = pyjstat.Dataset.read(response.text)
# print(dataset)
df = dataset.write('dataframe')
df.head()
df.tail()
df.info()
df.plot()
print(type(df.head()))
print(type(df.tail()))
print(type(df.info()))
print(type(df.plot()))



### Notes to self
# "filter" : "item" gir enkeltverdier
# "filter" : "top", "values": ["3"] gir 3 siste tidspunkt ("Tid")
# "filter" : "all", "values": ["*"]
# response-format: also suppoerts, csv2, csv3, xlsx