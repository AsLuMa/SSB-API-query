'''Data frå SSB henta 16.12.2021, klokka 19.36
Skript for å øve på databehandling frå fil, for å unngå mange queries til API-et'''

import pandas as pd
from pyjstat import pyjstat
import requests
import time
import json
import matplotlib.pyplot as plt

df_fastlege = pd.read_csv('temp_storage.txt')
print(df_fastlege.to_string())



