'''
Practice script to fetch, process and display information from Statistisk Sentralbyrå (SSB), using their API
https://www.ssb.no/api
Data fetched from table 04511: Psykisk helsevern for voksne. Døgnplasser, utskrivninger, oppholdsdøgn, polikliniske konsultasjoner og oppholdsdager, etter helseforetak 1990 - 2020
https://www.ssb.no/statbank/table/04511/
Kodeeksempel frå SSB: https://www.ssb.no/omssb/tjenester-og-verktoy/api/px-api/eksempler-pa-kode
R also has support for JSON-stat
'''

# API-console to autogenerate JSON-stat queries (sometimes doesn't give the right query-code!)
# https://data.ssb.no/api/v0/no/console

### List of data to fetch/goals for script:
# Trends from 2002-2020 (no data before 2002) for HELSEREGION VEST TOTALT (rates pr 1000):
# - oppholdsdager
# - polikliniske konsultasjoner


# ---- # KODE
import pandas as pd
from pyjstat import pyjstat
import requests
import time
import json
import matplotlib.pyplot as plt

time.sleep(4)


POST_URL = 'https://data.ssb.no/api/v0/no/table/04511'

# Helseregion Vest
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
          "Dognplasser",
          "Oppholdsdgn",
          "PolikliniskeKonsul"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "top",
        "values": [
          "19"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

response = requests.post(POST_URL, json=helseregion_vest_totalt_query)

# Returns and reads Pandas-dataframe
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write('dataframe')



# Sets 'år' (year) as index variable
# TODO can this be refactored?
df_dplasser = df[df['statistikkvariabel'] == 'Døgnplasser']
df_dplasser_indexed = df_dplasser.set_index('år')

df_oppholdsdogn = df[df['statistikkvariabel'] == 'Oppholdsdøgn']
df_oppholdsdogn_indexed = df_oppholdsdogn.set_index('år')

df_polikliniske_konsultasjoner = df[df['statistikkvariabel'] == 'Polikliniske konsultasjoner']
df_polikliniske_konsultasjoner_indexed = df_polikliniske_konsultasjoner.set_index('år')



def show_figure():
  fig, ax = plt.subplots()
  # y1 = df_dplasser_indexed.plot(y='value') # råtalet var for lav til at det var meiningsfult å inkludere
  df_oppholdsdogn_indexed.plot(ax=ax, y='value', label="Oppholdsdøgn")
  df_polikliniske_konsultasjoner_indexed.plot(ax=ax, y='value', label="Polikliniske konsultasjoner")
  ax.set_ylim(ymin=0)
  plt.show()

show_figure()

# ---- # Notes to self
# "filter" : "item" gir enkeltverdier
# "filter" : "top", "values": ["3"] gir 3 siste tidspunkt ("Tid")
# "filter" : "all", "values": ["*"]
# response-format: also suppoerts, csv2, csv3, xlsx

# ---- # Superflous code

### Pretty print of data - does not encode norwegian letters correctly, but that's not super important since the purpose of this code is just to get an overview of the data
# string_of_data = response.text
# temp_string_for_prettyprint = json.loads(string_of_data)
# print(json.dumps(temp_string_for_prettyprint, indent=4, sort_keys=True))
