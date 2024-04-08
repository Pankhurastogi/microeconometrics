import pandas as pd
import numpy as np

df = pd.read_excel("./../dataset/fiw.xlsx", sheet_name = "Ratings")
# print(df.head(10))
print(f"Number of rows before eliminating: {df.shape[0]}")
for index, row in df.iterrows():
    if index >= 0:
        if 'NF' in row.values or '-' in row.values:
            df.drop(index, inplace=True)

df.reset_index(drop=True, inplace=True)

df.to_csv("demo.csv", index=False)

columns = range(2, len(df.columns), 6)
transitions=np.zeros(df.shape[0]-1)

for index, row in df.iterrows():
    if index<1: 
        continue
    for column in columns:
        if column+3 >= len(df.columns):
            break
        status_first = row.iloc[column]
        status_next = row.iloc[column+3]
        if status_first != status_next:
            transitions[index-1]=1
            break

print(f"Number of rows after eliminating: {df.shape[0]}")
country_names = df.iloc[1:, 0].tolist()
country_name_series = pd.Series(country_names)
transition_column = pd.Series(transitions)
df_country_name = pd.DataFrame({'Country_Name': country_name_series, 'Transition': transition_column})
df_country_name.to_csv("../democratic_countries.csv", index=False)