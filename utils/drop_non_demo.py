import pandas as pd

countries_list = pd.read_csv("democratic_countries.csv")["Country_Name"]
data = pd.read_csv("../full_data.csv")

filtered_data = data[data["Country_Name"].isin(countries_list)]
filtered_data.to_csv("../filtered_full_data.csv", index=False)

print("Filtered data has been saved to filtered_data.csv")

