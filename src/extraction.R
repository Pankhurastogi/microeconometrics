#Source the function
source("rename_cols.R")

#Read datasets
wave1 = read.csv("~/Documents/microecon/dataset/WV1_fixed.csv")
wave2 = read.csv("~/Documents/microecon/dataset/WV2_fixed.csv")
wave3 = read.csv("~/Documents/microecon/dataset/WV3_fixed.csv")
wave4 = read.csv("~/Documents/microecon/dataset/WV4.csv")
wave5 = read.csv("~/Documents/microecon/dataset/WV5_fixed.csv")

#Extract data of columns of interest
wave1_interest = wave1[,c("V1", "V2", "V214", "V32", "V118", "V119", "V121", "V120", "V37", "V216", "V89", "V220", "V90", "Y002")]
wave2_interest = wave2[,c("V1", "V2", "V353", "V23", "V242", "V243", "V244", "V245", "V10", "V355", "V181", "V358", "V211", "V375", "V377")]
wave3_interest = wave3[,c("V1", "V2", "V214", "V32", "V118", "V119", "V121", "V120", "V37", "V216", "V89", "V220", "V90", "V217", "V238")]
wave4_interest = wave4[,c("V1", "V2", "V223", "V43", "V134", "V135", "V136", "V137", "V32","V225", "V106", "V229", "V107", "V226", "V246")]
wave5_interest = wave5[,c("V1", "V2", "V235", "V28", "V96", "V97", "V98", "V99","V237", "V55", "V231", "V56", "V238", "V260")]
wave5_interest$V37 <- rep(0, nrow(wave5_interest))
wave1_interest$V217 <- rep(0, nrow(wave1_interest))

#Remove missing data from the extracted data 
wave1_interest = wave1_interest[complete.cases(wave1_interest),]
wave2_interest = wave2_interest[complete.cases(wave2_interest),]
wave3_interest = wave3_interest[complete.cases(wave3_interest),]
wave4_interest = wave4_interest[complete.cases(wave4_interest),]

#Make dictionaries to map column names 
wv1_wv2_map <- list(
  "V1" = "V1",
  "V2" = "V2",
  "V214" = "V353",
  "V32" = "V23",
  "V118" = "V242",
  "V119" = "V243",
  "V121" = "V245",
  "V120" = "V244",
  "V37" = "V10",
  "V216" = "V355",
  "V89" = "V181",
  "V220" = "V358",
  "V90" = "V211",
  "V217" = "V375",
  "Y002" = "V377"
)

wv1_wv3_map <- list(
  "Y002" = "V238"
)

wv1_wv4_map <- list(
  "V1" = "V1",
  "V2" = "V2",
  "V37" = "V32",
  "V214" = "V223",
  "V32" = "V43",
  "V118" = "V134",
  "V119" = "V135",
  "V120" = "V136",
  "V121" = "V137",
  "V216" = "V225",
  "V89" = "V106",
  "V220" = "V229",
  "V90" = "V107",
  "V217" = "V226",
  "Y002" = "V246"
)

wv1_wv5_map <- list(
  "V1" = "V1",
  "V2" = "V2",
  "V37" = "V37",
  "V214" = "V235",
  "V32" = "V28",
  "V118" = "V96",
  "V119" = "V97",
  "V120" = "V98",
  "V121" = "V99",
  "V216" = "V237",
  "V89" = "V55",
  "V220" = "V231",
  "V90" = "V56",
  "V217" = "V238",
  "Y002" = "V260"
)

wave1_renamed = wave1_interest
wave2_renamed = rename_columns(wave2_interest, wv1_wv2_map)
wave3_renamed = rename_columns(wave3_interest, wv1_wv3_map)
wave4_renamed = rename_columns(wave4_interest, wv1_wv4_map)
wave5_renamed = rename_columns(wave5_interest, wv1_wv5_map)

#Append the renamed wave datasets, remove missing (-ve) values, and merge country names 
full_data = rbind(wave1_renamed, wave2_renamed, wave3_renamed, wave4_renamed, wave5_renamed)
#cleaned_data <- subset(full_data, !apply(full_data, 1, function(row) any(row < 0)))
cleaned_data <- full_data

#Drop entries with country name as NA 
cleaned_data <- cleaned_data[!is.na(cleaned_data$"V2"), ]

#Drop entries with invalid data for year
cleaned_data <- cleaned_data[cleaned_data$"Y002" >= 1980, ]

#Export the appended dataset into a csv file
file_path = "~/Documents/microecon/full_data.csv"
write.csv(cleaned_data, file=file_path, row.names = FALSE)
print(paste("Dataset exported to:", file_path))

