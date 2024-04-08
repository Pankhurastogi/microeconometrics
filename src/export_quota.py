import pandas as pd
import numpy as np
import tqdm as tqdm
import os 

rel_path = os.path.relpath("~/Documents/microecon/dataset/", "~/Documents/microecon/src/")
df = pd.read_csv(os.path.join(rel_path, "quota.csv"))
countries = df['country'].unique().tolist()
print(f"Total number of countries in dataset: {len(countries)}")
years=np.zeros(len(countries))
country_index = 0

for country in countries:
    filtered_df = df[df['country'] == country]
    # print(filtered_df.head())
    num_rows = len(filtered_df)
    for i in range(num_rows-1):
        current_row = filtered_df.iloc[i]
        next_row = filtered_df.iloc[i+1]
        if current_row.iloc[2] == 0 and next_row.iloc[2] == 1:
            years[country_index] = next_row.iloc[1]
            break
    print(f"Country: {country}, Year: {years[country_index]}")
    country_index=country_index+1

print(years)
print(f"Total number of years extracted: {len(years)}")

country_name_series = pd.Series(countries)
year_series = pd.Series(years)
df_quota = pd.DataFrame({'Country_Name': country_name_series, 'Year': year_series})

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
full_data_df = pd.read_csv(os.path.join(rel_path, "full_data_countries.csv"))
our_countries = full_data_df['Country_Name'].unique().tolist()
print(len(our_countries))

filtered_df = pd.DataFrame()
filtered_full_df = pd.DataFrame()
for country in our_countries:
    if country in df_quota["Country_Name"].tolist():
        temp_df = df_quota[df_quota["Country_Name"]==country]
        filtered_df = pd.concat([filtered_df, temp_df])
        temp_full_df = full_data_df[full_data_df['Country_Name']==country]
        filtered_full_df = pd.concat([filtered_full_df, temp_full_df])

for index, row in filtered_df.iterrows():
    if row.iloc[1]==0:
        continue
    if row.iloc[1]<=1980 or row.iloc[1]>=2010:
        filtered_df.loc[index, 'Year']=0

print(len(filtered_full_df["Country_Name"].unique().tolist()))
df_quota = filtered_df

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
df_quota.to_csv(os.path.join(rel_path, "quota_years.csv"), index=False)
filtered_full_df.to_csv(os.path.join(rel_path, "filtered_full_data.csv"), index=False)