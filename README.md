# Microeconometrics project, University of Manchester 2024

## Dataset extraction and analysis code for Microeconometrics project

This project aims to look at the effect of quotas on Women's political participation. The codes in this GitHub repository are for extracting, cleaning and analysing data from the [World Values Survey (WVS) dataset](https://www.worldvaluessurvey.org/wvs.jsp) for data on political participation, education, employment, marital status, children, etc and the [QaROT dataset](https://www.openicpsr.org/openicpsr/project/100918/version/V1/view) for data on quotas in various countries. 

R version 4.2.2 and Python version 3.11.4 has been used. 

The project directory structure is organized as follows:

```bash
├── dataset
│   └── quota.csv
├── metadata
│   ├── codebook.txt
│   ├── control.txt
│   ├── final_countries_list.txt
│   ├── merged_countries.csv
│   ├── merged_country_data.csv
│   ├── treatment.txt
│   ├── wv1_countries.csv
│   ├── wv1_countries.txt
│   ├── wv2_countries.csv
│   ├── wv2_countries.txt
│   ├── wv3_countries.csv
│   ├── wv3_countries.txt
│   ├── wv4_countries.csv
│   ├── wv4_countries.txt
│   ├── wv5_countries.csv
│   └── wv5_countries.txt
├── README.md
├── requirements.txt
├── src
│   ├── add_country.py
│   ├── dataset_gen.py
│   ├── export_quota.py
│   ├── extraction.R
│   ├── join_dataset.py
│   ├── micrecon_Rcode_analysis.R
│   ├── plotting.py
│   └── rename_cols.R
└── utils
    ├── data_exploration.ipynb
    ├── drop_non_demo.py
    ├── fix_waves.py
    ├── merge.py
    ├── parse_countries.py
    └── read_fiw.py
```

The `utils` folder contains utility/helper code which is used in the extraction of data. `src` folder contains actual code for extraction and analysis. The `metadata` folder is used to contain additional data about the datasets that were generated during dataset extraction process and will be helpful for analysis. 

Following are the steps to run the code on actual dataset. 

## Setting up the python environment
- Install Python, set up a new virtual environment
- Run the following command to install all python packages required for running this code: `pip install -r requirements.txt`

## Dataset download
- Download the `.csv` files of the WVS dataset for WVS 1 through 5. This code takes all 5 datasets so it is required to download all. 
- Download the `.csv` file of the QaROT dataset
- Create a folder called `dataset` in the main folder and put the datasets there.
- Rename the WVS datasets as `WV1.csv`, `WV2.csv` and so on. 
- Rename the QaROT dataset as `quota.csv`
- For ease of usage the quota dataset is provided in this repository in the dataset folder

## Change path in R file
-  The code was written in Linux and absolute path is used. Before using the code, the path needs to be changed to actual path in your system. 
- Navigate to the `extraction.R` file in the `utils` folder. Change the path `~/Documents/microecon/dataset/` to your original path in the `read.csv()` function and `write.csv()` function. 
At the beginning of the file: 
    ```
    wave1 = read.csv("~/Documents/microecon/dataset/WV1_fixed.csv")
    wave2 = read.csv("~/Documents/microecon/dataset/WV2_fixed.csv")
    wave3 = read.csv("~/Documents/microecon/dataset/WV3_fixed.csv")
    wave4 = read.csv("~/Documents/microecon/dataset/WV4.csv")
    wave5 = read.csv("~/Documents/microecon/dataset/WV5_fixed.csv")
    ``` 
    and at the end of the file:
    ```
    file_path = "~/Documents/microecon/full_data.csv"
    write.csv(cleaned_data, file=file_path, row.names = FALSE)
    ```

## Fix WVS dataset 
- Change directory to utils by using command `cd utils`
- Year data in WV1, WV2, WV3, and WV5 are messed up. To clean the data, run the following command in your terminal after activating the virtual environment. 
    ```python3 fix_waves.py```
    This will fix the datasets and generate new files in the `dataset/` folder called `WV#_fixed.csv`.

## Run R extraction code
- Change directory to src from main directory by using command `cd src`
- Run the `extraction.R` file using the command `Rscript extraction.R` to extract data and store it as `full_data.csv`

## Add countries
- Change directory to src from main directory by using command `cd src`
- Run the following command to add country labels to your data. 
`python3 add_country.py` 
- It will generate a file called `full_data_countries.csv`

## Export quota 
- Change directory to src from main directory by using command `cd src`
- To parse the quota dataset, run the following command:
`python3 export_quota.py`
- It will generate two files called `quota_years.csv` and `filtered_full_data.csv` 

## Join WVS and QaROT dataset
- Change directory to src from main directory by using command `cd src`
- To join the datasets into a final file, run the following command:
`python3 join_dataset.py`
- It will generate a file called `full_data_plus_quota.csv`


## Form the final dataset
- Change directory to src from main directory by using command `cd src`
- To generate the final total and DID datasets, run the following command:
`python3 dataset_gen.py`
- It will generate two files: `DID_all_removed.csv` and `final_dataset.csv`

## Plotting
- Change directory to src from main directory by using command `cd src`
- For plotting, create a new directory called `images` in the main directory. 
- Run the following command:
`python3 plotting.py`

## Analysis 
- Change directory to src from main directory by using command `cd src`
- Before running the R, code change the path in `quota_data <- read.csv("~/Documents/microecon/final_dataset.csv")` to your path.
- To perform analysis, run the command: 
`Rscript micrecon_Rcode_analysis.R`