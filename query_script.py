import time
import pandas
import requests as req

time.sleep(3)

# POST-URL example:
# https://data.ssb.no/api-navn/api-versjon/språk/

# Information about the API (from SSB, in Norwegian)
# Grensene per uttrekk er 800.000 dataceller og antall spørringer er 30 per 60. sekund.
# unngå tidsrommet 07.55 – 08.15

# Døde, etter kjønn og ettårig alder, 1986 - siste år
# Dødssårsaksregisteret har migrert til FHI, som ikkje har API
url_str = 'https://data.ssb.no/api/v0/dataset/567324.json?lang=no'

# Request data from specific table
# url_str = 'https://www.ssb.no/statbank/table/10325'






