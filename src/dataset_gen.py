import pandas as pd 
import numpy as np
import os

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
df = pd.read_csv(os.path.join(rel_path, "full_data_plus_quota.csv"))

#Rename df
old_names = ["V1","code","V214","V32","V118","V119","V121","V120","V37", "V216", "V89", "V220", "V90", "Y002", "V217", "Country_Name","Year"]
new_names = ["wave", "code", "sex", "member", "petition", "boycott", "other", "demonstration", "discussion", "age", "marital_status", "employment", "children", "year", "education", "country_name", "quota_year"]
rename_dict = {old_name:new_name for old_name, new_name in zip(old_names, new_names)}
renamed_df = df.rename(columns=rename_dict)

#Set datatype of values
dtype_dict =  { 'wave': 'int64', 
                'code': 'int64', 
                'sex': 'int64',
                'member':'int64',
                'petition':'int64',
                'boycott':'int64',
                'other':'int64',
                'demonstration':'int64',
                'discussion':'int64',
                'age':'int64',
                'marital_status':'int64',
                'employment':'int64',
                'children':'int64',
                'year':'int64',
                'education':'int64',
                'country_name':'str',
                'quota_year':'int64'
                }

renamed_df = renamed_df.astype(dtype_dict)
did_df = renamed_df

#Find list of control group and treatment group countries and store them in files
treatment_group = []
control_group = []

our_countries = renamed_df['country_name'].unique().tolist()

for country in our_countries:
    country_df = renamed_df[renamed_df['country_name']==country] 
    quota_year_country = int(country_df['quota_year'].iloc[0])
    if quota_year_country == 0:
        control_group.append(country)
    else:
        treatment_group.append(country)

print(f"Treatment group :{treatment_group}, length = {len(treatment_group)}")
print(f"Control group : {control_group}, length = {len(control_group)}")

#Write into text files
rel_path = os.path.relpath("~/Documents/microecon/metadata/", "~/Documents/microecon/src/")
with open(os.path.join(rel_path, "treatment.txt"), "w") as file:
    for country in treatment_group:
        file.write(country + "\n")

with open(os.path.join(rel_path, "control.txt"), "w") as file:
    for country in control_group:
        file.write(country + "\n")

#Remove all -2, -4
numeric_columns = renamed_df.select_dtypes(include=['int64'])
dropped_df = renamed_df[(numeric_columns >= 0).all(axis=1)]

#Define functions for applying to different columns
def map_sex(value):
    if value==2:
        return 1
    else:
        return 0

def map_quota(value):
    if value>1980:
        return 1
    else:
        return 0

#mapping functions for education
def education_primary_inc(value):
    if value==2:
        return 1
    else:
        return 0

def education_primary_comp(value):
    if value==3:
        return 1
    else:
        return 0
    
def education_secondary_inc(value):
    if value==4:
        return 1
    else:
        return 0

def education_secondary_comp(value):
    if value==5:
        return 1
    else:
        return 0

def education_some_uni(value):
    if value==8:
        return 1
    else:
        return 0

def education_uni_degree(value):
    if value==9:
        return 1
    else:
        return 0

#Map functions for employment
def employment_bin(value):
    if value in [1,2,3]:
        return 1
    else:
        return 0

def employment_retired(value):
    if value==4:
        return 1
    else:
        return 0

def employment_housewife(value):
    if value==5:
        return 1
    else:
        return 0

def employment_student(value):
    if value==6:
        return 1
    else:
        return 0

def employment_unemployed(value):
    if value==7:
        return 1
    else:
        return 0

def married(value):
    if value==1:
        return 1
    else:
        return 0

def children(value):
    if value>0:
        return 1
    else:
        return 0

def map_membership(row):
    if row['wave'] in [1,3,5]:
        if row['member'] in [1,2]:
            return 1
        else:
            return 0
    else:
        if row['member']==1:
            return 1
        else: 
            return 0

def map_political_action(value):
    if value in [1,2]:
        return 1
    else:
        return 0

dropped_df['sex_bin'] = dropped_df['sex'].apply(map_sex)
dropped_df['quota'] = dropped_df['quota_year'].apply(map_quota)
dropped_df['primary_incomplete'] = dropped_df['education'].apply(education_primary_inc)
dropped_df['primary_complete'] = dropped_df['education'].apply(education_primary_comp)
dropped_df['secondary_incomplete'] = dropped_df['education'].apply(education_secondary_inc)
dropped_df['secondary_complete'] = dropped_df['education'].apply(education_secondary_comp)
dropped_df['some_university'] = dropped_df['education'].apply(education_some_uni)
dropped_df['university_degree'] = dropped_df['education'].apply(education_uni_degree)
dropped_df['employed_bin'] = dropped_df['employment'].apply(employment_bin)
dropped_df['retired'] = dropped_df['employment'].apply(employment_retired)
dropped_df['housewife'] = dropped_df['employment'].apply(employment_housewife)
dropped_df['student'] = dropped_df['employment'].apply(employment_student)
dropped_df['unemployed'] = dropped_df['employment'].apply(employment_unemployed)
dropped_df['married_bin'] = dropped_df['marital_status'].apply(married)
dropped_df['children_bin'] = dropped_df['children'].apply(children)
dropped_df['membership_bin'] = dropped_df.apply(map_membership, axis=1)
dropped_df['petition_bin'] = dropped_df['petition'].apply(map_political_action)
dropped_df['boycott_bin'] = dropped_df['boycott'].apply(map_political_action)
dropped_df['demonstration_bin'] = dropped_df['demonstration'].apply(map_political_action)
dropped_df['other_bin'] = dropped_df['other'].apply(map_political_action)

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
dropped_df.to_csv(os.path.join(rel_path, "final_dataset.csv"), index=False)

#DID file generation

final_data_df = pd.read_csv(os.path.join(rel_path, "final_dataset.csv"))
countries = final_data_df['country_name'].unique().tolist()
filtered_did_df = pd.DataFrame()
for country in countries:
    country_df = final_data_df[final_data_df['country_name']==country]
    years = country_df['year'].unique().tolist()
    print(f"\nCountry: {country}, Years: {years}")
    if len(years) >=3:
        print(f"Data available for {len(years)} years. Keeping...")
        filtered_did_df = pd.concat([filtered_did_df, country_df])

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
filtered_did_df.to_csv(os.path.join(rel_path, "DID_all_removed.csv"), index=False)