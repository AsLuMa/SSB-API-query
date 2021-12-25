import numpy as np
import pandas as pd

# numerical index always available?
df_yh = pd.read_csv('yrkesrelaterte_helseplager.txt', nrows=500)
# print(df_yh.to_string())

# ---- # grouping, appending and sorting by column

group_1 = df_yh.groupby(by=['kjønn', 'yrke', 'år'], as_index=True)
df1 = group_1.get_group(('Menn', 'Alle yrker', 2019)).drop(columns='statistikkvariabel')
df2 = group_1.get_group(('Menn', 'Ledere', 2019)).drop(columns='statistikkvariabel')
# print(df1.head(20).to_string())
# print(df2.head(20).to_string())

df_appended = df1.append(df2)
df_sorted = df_appended.sort_values(by='type helseproblem', axis=0)
df_sorted = df_sorted.set_index('type helseproblem')
# df_all_values = df_sorted['value']
# print(df_appended.to_string())
# print(df_sorted.to_string())
# print(df_all_values)

def menn_yrke_values(df, yrke):
    return_df = df.loc[(df['kjønn'] == 'Menn') & (df['yrke'] == yrke)]['value']
    print(return_df.to_string())
    return return_df

menn_yrke_values(df_sorted, 'Alle yrker')
# menn_yrke_values(df_sorted, 'Ledere')

# df_menn_value = df_sorted.loc[(df_sorted['kjønn'] == 'Menn') & (df_sorted['yrke'] == 'Alle yrker')]['value']
# print(df_menn_value.to_string())

# ---- # Plot dat shizz



# ---- # fetching by loc, iloc, columns

# # df_yh = df_yh.set_index('yrke')
# # print("index after", df_yh.index)
# # print(df_yh.head(3).to_string())
#
# # df_index_nr = df_yh.iloc[list(range(5)), 3:]
# # print("df index nr", df_index_nr.index)
# # print("df_index_nr", df_index_nr)
#
# # print(df_yh.columns)
#
# df_yrke_kjønn = df_yh[['yrke', 'kjønn', 'value', 'type helseproblem', 'år']]
# # print(df_yrke_kjønn.head(20).to_string())
#
# df_yrke_kjønn = df_yrke_kjønn.set_index(['yrke', 'value'])
# # print(df_yrke_kjønn.to_string())
# # index - locate row from index
# df_test = df_yrke_kjønn.loc[['Alle yrker', 'Ledere']]
# # print(df_test.to_string())
#
# df_menn = df_test.loc[(df_test['kjønn'] == 'Menn') & (df_test['år'] == 2019)] #TODO ['value']
# print(df_menn.to_string())


