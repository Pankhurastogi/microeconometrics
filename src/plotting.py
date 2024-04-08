import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

rel_path = os.path.relpath("~/Documents/microecon/", "~/Documents/microecon/src/")
df = pd.read_csv(os.path.join(rel_path, "DID_all_removed.csv"))

#Plot for petition, boycott, demonstration, other 
col_title_dict = {'petition': 'Have filed a petition', 'boycott': 'Have participated in an unofficial boycott', 'demonstration': 'Have participated in demonstration', 'other': 'Have taken other political action'}

countries = df['country_name'].unique().tolist()

for country in countries:
    print(f"Plotting for {country}...")
    country_df = df[df['country_name']==country]
    years = country_df['year'].unique().tolist()
    quota_year = country_df['quota_year'].iloc[0]
    for column, title in col_title_dict.items():
        men= np.zeros(len(years))
        women = np.zeros(len(years))
        for index, year in enumerate(years):
            total_men = country_df[(country_df['sex_bin']==0) & (country_df['year']==year)][column].count()
            total_women = country_df[(country_df['sex_bin']==1) & (country_df['year']==year)][column].count()
            men[index] = country_df[(country_df['sex_bin']==0) & (country_df['year']==year) & (country_df[column]==1)].count().iloc[0]
            women[index] = country_df[(country_df['sex_bin']==1) & (country_df['year']==year) & (country_df[column]==1)].count().iloc[0]
            men[index] = (men[index]/total_men)*100
            women[index] = (women[index]/total_women)*100

        #Plotting
        plt.clf()
        plt.figure(figsize=(5, 3))
        plt.plot(years, men, label="Men", marker='*', linestyle = '-', linewidth = 2, alpha=0.7)
        plt.plot(years, women, label="Women", marker='o', linestyle = '-', linewidth = 2, alpha=0.7)
        plt.xlabel("Year")
        plt.ylabel("Percentage of respondents")
        plt.title(f"{title}\n{country}")
        plt.legend()
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        if quota_year>0:
            plt.axvline(x=quota_year, color='black', linestyle='-', label = 'Quota', linewidth=1)
            if country=='Australia':
                plt.xticks(years)
            else:
                plt.xticks(years+[quota_year])
        else:
            plt.xticks(years)
        plt.tight_layout()
        rel_path = os.path.relpath("~/Documents/microecon/images/", "~/Documents/microecon/src/")
        image_path = os.path.join(rel_path, f"{country}_{column}.png")
        plt.savefig(image_path, dpi=300)


#Plot for membership
for country in countries:
    print(f"Plotting membership for {country}...")
    country_df = df[df['country_name']==country]
    years = country_df['year'].unique().tolist()
    quota_year = country_df['quota_year'].iloc[0]
    men= np.zeros(len(years))
    women = np.zeros(len(years))
    for index, year in enumerate(years):
        total_men = country_df[(country_df['sex_bin']==0) & (country_df['year']==year)][column].count()
        total_women = country_df[(country_df['sex_bin']==1) & (country_df['year']==year)][column].count()
        
        men[index] = country_df[(country_df['sex_bin']==0) & (country_df['year']==year)]['membership_bin'].sum()
        women[index] = country_df[(country_df['sex_bin']==1) & (country_df['year']==year)]['membership_bin'].sum()
        
        men[index] = (men[index]/total_men)*100
        women[index] = (women[index]/total_women)*100
    
    #Plotting
    plt.clf()
    plt.figure(figsize=(5, 3))
    plt.plot(years, men, label="Men", marker='*', linestyle = '-', linewidth = 2, alpha=0.7)
    plt.plot(years, women, label="Women", marker='o', linestyle = '-', linewidth = 2, alpha=0.7)
    plt.xlabel("Year")
    plt.ylabel("Percentage of respondents")
    plt.title(f"Have been an active/inactive member of a political party\n{country}")
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    if quota_year>0:
        plt.axvline(x=quota_year, color='black', linestyle='-', label = 'Quota', linewidth=1)
        if country=='Australia':
            plt.xticks(years)
        else:
            plt.xticks(years+[quota_year])
    else:
        plt.xticks(years)
    plt.tight_layout()
    rel_path = os.path.relpath("~/Documents/microecon/images/", "~/Documents/microecon/src/")
    image_path = os.path.join(rel_path, f"{country}_membership.png")
    plt.savefig(image_path, dpi=300)