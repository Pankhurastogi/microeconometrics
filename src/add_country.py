import pandas as pd
import numpy as np
import tqdm as tqdm 
import os

absolute_path = "~/Documents/microecon/"
base_path = "~/Documents/microecon/utils/"
rel_path = os.path.relpath(absolute_path, base_path)
full_data_path = os.path.join(rel_path, "full_data.csv")

country_data_path = os.path.join(os.path.relpath("~/Documents/microecon/metadata/", 
                                                "~/Documents/microecon/src/"), 
                                                "merged_country_data.csv")

full_data_df = pd.read_csv(full_data_path)
country_df = pd.read_csv(country_data_path)
full_data_df = full_data_df.rename(columns={'V2': 'code'})
country_df = country_df.rename(columns={'Country_Code': 'code'})

merged_df = pd.merge(full_data_df, country_df, on='code', how='left')

final_path = os.path.join(os.path.relpath("~/Documents/microecon/", 
                                                "~/Documents/microecon/src/"), 
                                                "full_data_countries.csv")
merged_df.to_csv(final_path, index=False)