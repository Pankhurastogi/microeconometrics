import pandas as pd

file_name = "wv5_countries" #Change this for different wave dataset
file_path = f"./../metadata/{file_name}.txt" 
with open(file_path, 'r') as file:
    data = file.readlines()

# Splitting the data into country code and country name
parsed_data = []
for line in data:
    # split_line = line.strip().split(".- ", 1) #For wave 1,2
    split_line = line.strip().split(" ", 1)     #For wave 3,4,5
    parsed_data.append(split_line)

# Converting the parsed data into a DataFrame
parsed_df = pd.DataFrame(parsed_data, columns=["Country_Code", "Country_Name"])

# Writing the DataFrame to a CSV file
parsed_df.to_csv(f"./../metadata/{file_name}.csv", index=False)

print("Data has been exported to country_data.csv")