import pandas as pd
file_paths = ["wv1_countries.csv", "wv2_countries.csv", "wv3_countries.csv", "wv4_countries.csv", "wv5_countries.csv"]
dfs = {}
for path in file_paths:
    df = pd.read_csv(f"./../metadata/{path}")
    dfs[path] = df

#Code for checking 
# Merge the DataFrames on the country code column
# merged_df = None
# for path, df in dfs.items():
#     if merged_df is None:
#         merged_df = df
#     else:
#         merged_df = pd.merge(merged_df, df, on="Country_Code", how="outer", suffixes=('', f'_{path}'))

# merged_df.to_csv(f"./../metadata/merged_countries.csv", index=False)

#Code for storing merged_df
uniqe_merged_df = pd.concat(dfs).drop_duplicates(subset="Country_Code")
uniqe_merged_df.to_csv("./../metdata/merged_country_data.csv", index=False)