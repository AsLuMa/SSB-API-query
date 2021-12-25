import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# numerical index always available?
df_yh = pd.read_csv('yrkesrelaterte_helseplager.txt').drop(columns='statistikkvariabel').dropna()
# print(df_yh.to_string())

# ---- # grouping, appending and sorting by column

def get_from_group(group, kjønn, yrke, årstall):
    df = group.get_group((kjønn, yrke, årstall))
    return df

group_1 = df_yh.groupby(by=['kjønn', 'yrke', 'år'], as_index=True)

df_menn_yrker = get_from_group(group_1, 'Menn', 'Alle yrker', 2019)
df_kvinner_yrker = get_from_group(group_1, 'Kvinner', 'Alle yrker', 2019)
df_begge_kjonn = get_from_group(group_1, 'Begge kjønn', 'Alle yrker', 2019)

df_menn_yrker = df_menn_yrker.set_index('type helseproblem')

print(df_menn_yrker.head(20).to_string())
print(df_begge_kjonn.head(20).to_string())
# --- # Two dataframes appended
# df2 = get_from_group(group_1, 'Menn', 'Ledere', 2019)
# print(df2.head(20).to_string())
# df_appended = df1.append(df2)
# df_sorted = df_appended.sort_values(by='type helseproblem', axis=0)
# df_sorted = df_sorted.set_index('type helseproblem')
# print(df_sorted.to_string())

def kjønn_yrke_values(df, kjønn, yrke):
    return_df = df.loc[(df['kjønn'] == kjønn) & (df['yrke'] == yrke)]['value']
    # print(return_df.to_string())
    return return_df


values_menn_alle_yrker = kjønn_yrke_values(df_menn_yrker, 'Menn', 'Alle yrker')
values_kvinner_alle_yrker = kjønn_yrke_values(df_kvinner_yrker, 'Kvinner', 'Alle yrker')
values_begge_alle_yrker = kjønn_yrke_values(df_begge_kjonn, 'Begge kjønn', 'Alle yrker')

print(len(values_begge_alle_yrker))
print(len(values_menn_alle_yrker))
print(len(values_kvinner_alle_yrker))

# Labels til y-akse
# liste_labels_y_akse = ["Hodepine/migrene", "Smerter armer", "Smerter bein", "Smerter nakke/øvre rygg", "Smerter nedre rygg"]

labelsall = values_menn_alle_yrker.index
print(type(labelsall))
width = 0.25
height = 0.10
x_indexes = np.arange(len(values_menn_alle_yrker))

# ---- # Plot dat shizz
plt.style.use('seaborn')
plt.title(f"Fancy schmancy tittel")
plt.barh(x_indexes-width, values_kvinner_alle_yrker, width, label="Kvinner, alle yrker")
plt.barh(x_indexes+width/2, values_menn_alle_yrker, width, align='edge', label="Menn, alle yrker")
plt.barh(x_indexes, values_begge_alle_yrker, width, label="Begge kjønn, alle yrker")
plt.yticks(ticks=x_indexes, labels=labelsall)
plt.xlim(0, 100)

# plt.bar(x_indexes - width, values_kvinner_alle_yrker, width=width, label="Kvinner, alle yrker")
# plt.bar(x_indexes, values_menn_alle_yrker, width=width, label="Menn, alle yrker")
# plt.bar(x_indexes + width, values_begge_alle_yrker, width=width, label="Begge kjønn, alle yrker")
# plt.xticks(ticks=x_indexes, labels=labelsall)
# plt.ylim(0, 100)

plt.xlabel("Prosent?")
plt.ylabel("Antall")

plt.legend()
plt.show()




exit()
# ---- # fetching by loc, iloc, columns

# df_yh = df_yh.set_index('yrke')
# print("index after", df_yh.index)
# print(df_yh.head(3).to_string())

# df_index_nr = df_yh.iloc[list(range(5)), 3:]
# print("df index nr", df_index_nr.index)
# print("df_index_nr", df_index_nr)

# print(df_yh.columns)

df_yrke_kjønn = df_yh[['yrke', 'kjønn', 'value', 'type helseproblem', 'år']]
# print(df_yrke_kjønn.head(20).to_string())

df_yrke_kjønn = df_yrke_kjønn.set_index(['yrke', 'value'])
# print(df_yrke_kjønn.to_string())
# index - locate row from index
df_test = df_yrke_kjønn.loc[['Alle yrker', 'Ledere']]
# print(df_test.to_string())

df_menn = df_test.loc[(df_test['kjønn'] == 'Menn') & (df_test['år'] == 2019)] #TODO ['value']
print(df_menn.to_string())


