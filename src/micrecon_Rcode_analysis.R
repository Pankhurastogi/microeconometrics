# Install the packages
library(plm)
library(lmtest)

#Read the data 
quota_data <- read.csv("~/Documents/microecon/final_dataset.csv")


#generating interaction term 
quota_data$quota_sex_interaction <- quota_data$quota * quota_data$sex_bin
head(quota_data)

#Normal Regression
#petition
simplereg = lm(petition_bin ~ quota + quota_sex_interaction + sex_bin +
            married_bin + children_bin + age + employed_bin + housewife +
            student + retired + unemployed + primary_complete + 
            primary_incomplete + secondary_complete + 
            secondary_incomplete + some_university +
            university_degree, data = quota_data)
summary(simplereg)

#Demonstrations 
simplereg = lm(demonstration_bin ~ quota + quota_sex_interaction + sex_bin +
                 married_bin + children_bin + age + employed_bin + housewife +
                 student + retired + unemployed + primary_complete + 
                 primary_incomplete + secondary_complete + 
                 secondary_incomplete + some_university +
                 university_degree, data = quota_data)
summary(simplereg)

#membership 
simplereg = lm(membership_bin ~ quota + quota_sex_interaction + sex_bin +
                 married_bin + children_bin + age + employed_bin + housewife +
                 student + retired + unemployed + primary_complete + 
                 primary_incomplete + secondary_complete + 
                 secondary_incomplete + some_university +
                 university_degree, data = quota_data)
summary(simplereg)

#boycotts
simplereg = lm(boycott_bin ~ quota + quota_sex_interaction + sex_bin +
                 married_bin + children_bin + age + employed_bin + housewife +
                 student + retired + unemployed + primary_complete + 
                 primary_incomplete + secondary_complete + 
                 secondary_incomplete + some_university +
                 university_degree, data = quota_data)
summary(simplereg)

#other political action
simplereg = lm(other_bin ~ quota + quota_sex_interaction + sex_bin +
                 married_bin + children_bin + age + employed_bin + housewife +
                 student + retired + unemployed + primary_complete + 
                 primary_incomplete + secondary_complete + 
                 secondary_incomplete + some_university +
                 university_degree, data = quota_data)
summary(simplereg)

#Country and Time fixed effects
quota_data$year <- as.factor(quota_data$year)
quota_data$country <- as.factor(quota_data$country_name)

#creating panel data object 
pdata <- plm.data(quota_data, index = c("country", "year"))

#Estimating Model with country and Time fixed effects
#petition 
fereg <- plm(petition_bin ~ quota + quota_sex_interaction + sex_bin +
             married_bin + children_bin + age + employed_bin + housewife +
             student + retired + unemployed + primary_complete + 
             primary_incomplete + secondary_complete + 
             secondary_incomplete + some_university +
            university_degree, data = pdata, model = "within", 
            effect = "twoways")
clustered_se <- coeftest(fereg, vcov = vcovHC(fereg, type = "HC1", cluster = "group"))
summary(fereg)
print(clustered_se)

#Demonstrations 
fereg <- plm(demonstration_bin ~ quota + quota_sex_interaction + sex_bin +
               married_bin + children_bin + age + employed_bin + housewife +
               student + retired + unemployed + primary_complete + 
               primary_incomplete + secondary_complete + 
               secondary_incomplete + some_university +
               university_degree, data = pdata, model = "within", 
             effect = "twoways")
clustered_se <- coeftest(fereg, vcov = vcovHC(fereg, type = "HC1", cluster = "group"))
summary(fereg)
print(clustered_se)

#membership
fereg <- plm(membership_bin ~ quota + quota_sex_interaction + sex_bin +
               married_bin + children_bin + age + employed_bin + housewife +
               student + retired + unemployed + primary_complete + 
               primary_incomplete + secondary_complete + 
               secondary_incomplete + some_university +
               university_degree, data = pdata, model = "within", 
             effect = "twoways")
clustered_se <- coeftest(fereg, vcov = vcovHC(fereg, type = "HC1", cluster = "group"))
summary(fereg)
print(clustered_se)

#boycotts
fereg <- plm(boycott_bin ~ quota + quota_sex_interaction + sex_bin +
               married_bin + children_bin + age + employed_bin + housewife +
               student + retired + unemployed + primary_complete + 
               primary_incomplete + secondary_complete + 
               secondary_incomplete + some_university +
               university_degree, data = pdata, model = "within", 
             effect = "twoways")
clustered_se <- coeftest(fereg, vcov = vcovHC(fereg, type = "HC1", cluster = "group"))
summary(fereg)
print(clustered_se)

#other political action 
fereg <- plm(other_bin ~ quota + quota_sex_interaction + sex_bin +
               married_bin + children_bin + age + employed_bin + housewife +
               student + retired + unemployed + primary_complete + 
               primary_incomplete + secondary_complete + 
               secondary_incomplete + some_university +
               university_degree, data = pdata, model = "within", 
             effect = "twoways")
clustered_se <- coeftest(fereg, vcov = vcovHC(fereg, type = "HC1", cluster = "group"))
summary(fereg)
print(clustered_se)







