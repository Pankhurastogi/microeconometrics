import pandas as pd
import numpy as np
import os

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
full_data = pd.read_csv(os.path.join(rel_path, "full_data_countries.csv"))
quota_years = pd.read_csv(os.path.join(rel_path, "quota_years.csv"))
# democracies = pd.read_csv("./../democratic_countries.csv")
merged_df = pd.merge(full_data, quota_years, on="Country_Name", how='inner')

countires = merged_df['Country_Name'].unique().tolist()

#Checking for data availability for over +/-1 year, if not : drop
filtered_df = pd.DataFrame()
n_treatment = 0
for country in countires:
    year = quota_years.loc[quota_years['Country_Name']==country,'Year'].iloc[0]
    years = merged_df[merged_df['Country_Name']==country]['Y002'].unique().tolist()
    # print(f"\nCountry={country}")
    # print(f"Years of data = {years}")
    # print(f"Quota year = {year}")
    if year==0:
        # print(f"Country = {country}")
        temp_df = merged_df[merged_df['Country_Name']==country]
        filtered_df = pd.concat([filtered_df, temp_df])
        # print("Taking this country...")
        continue

    if year > min(years) and year < max(years):
        # print("Taking this country...")
        n_treatment=n_treatment+1
        temp_df = merged_df[merged_df['Country_Name']==country]
        filtered_df = pd.concat([filtered_df, temp_df])

merged_df = filtered_df
print(f"No. of countries taken in Treatment group = {n_treatment}")
print(merged_df.shape)

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
merged_df.to_csv(os.path.join(rel_path, "full_data_plus_quota.csv"), index=False)