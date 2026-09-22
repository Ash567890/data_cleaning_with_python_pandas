# Complete cleaning of Table cust_az12 using pandas 

import pandas as pd
import numpy as np

cust_az12 = pd.read_csv(r"D:\SQL resource\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_erp\CUST_AZ12.csv")

cust_az12.head(10)

cust_az12[cust_az12.CID.isna()]

cust_az12[cust_az12.BDATE.isna()]

cust_az12[cust_az12.GEN.isna()]

I want to check the birth date (some birth dates are very old)

cust_az12["birthdate"]= pd.to_datetime(cust_az12.BDATE, errors='coerce')

This intermediate data is called cust_az12_f

cust_az12_f = cust_az12[cust_az12.birthdate >= "1930-01-01"]

cust_az12_f

Now, I want to transform the required column

cust_az12_f['cust-id']= cust_az12_f.CID.replace(r'^NAS','', regex=True)

cust_az12_f[cust_az12_f["cust-id"].str.contains(r"^NAS", regex=True)]

Now it is important to understand the values in the low-cardinality column

cust_az12_f.GEN.unique()

cust_az12_f["gender"]= cust_az12_f.GEN.str.strip().replace({'M':'Male', 'F':'Female','':'n/a', np.nan:'n/a'}) 

Changing the name of a column

cust_az12_f.rename(columns={'cust-id':'cust_id'}, inplace=True)

Now I want to load this file into a folder

cust_az12_f2= cust_az12_f[['cust_id', 'birthdate', 'gender']]

cust_az12_f2.to_csv(r'D:\Downloads\data_analytics_data\cust_az12_c.csv', index = None)

########################################################################################################################
LOC_A101 table cleaning 
########################################################################################################################

loc_a101 = pd.read_csv(r"D:\SQL resource\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_erp\LOC_A101.csv")

# Checking for null and empty values

loc_a101[loc_a101.CID == 'NaN']

loc_a101[loc_a101['CID'].isnull()]

# Checking for leading and trailing whitespace

loc_a101[loc_a101.CID == loc_a101.CID.str.strip]

loc_a101['cust_id']= loc_a101['CID'].replace(r'-','', regex=True)

# Running a test to check the quality

loc_a101[loc_a101.cust_id.str.contains(r'-', regex=True)]

loc_a101[loc_a101.CID.str.startswith('AW')==False]

# Checking country cardinality

loc_a101['CNTRY'].unique()

loc_a101["country"]= loc_a101['CNTRY'].str.strip().replace({'DE':"Germany", 'US':'United States', 'USA':'United States', np.nan:'n/a', '':'n/a'})

loc_a101.country.unique()

loc_a101_c = loc_a101[['cust_id', 'country']]

loc_a101_c

loc_a101_c.to_csv(r'D:\Downloads\data_analytics_data\loc_a101_c.csv', index = None)

##############################################################################################################
Customer Table cleaning
##############################################################################################################

customers = pd.read_csv(r"D:\SQL resource\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\cust_info.csv")

customers

# Checking for null values (NaN)

customer = customers[customers.cst_id.isnull() == False]

customer[customer.cst_id.isnull()]

customer[customer['cst_key'].isnull()]

# Checking for cst_key quality

customer[customer['cst_key'].str.contains(r'^AW', regex = True)== False]

# Null or nan

customer[customer.cst_firstname.isnull()]

# Treating Null values

customer.loc[customer.cst_firstname.isnull(), 'cst_firstname'] = customer.cst_lastname

customer[customer.cst_firstname.isnull()]

customer.dropna(subset=['cst_firstname'], inplace= True)

customer[customer.cst_firstname.isnull()]

# Checking for leading and trailing whitespace

customer.cst_firstname == customer.cst_firstname.str.strip()

customer['first_name']= customer.cst_firstname.str.strip().str.title()

customer['last_name']= customer.cst_lastname.str.strip().str.title().replace(np.nan, 'n/a')

customer[(customer.first_name == customer.first_name.str.strip())== False]

customer.last_name == customer.last_name.str.strip()

# Concatenating the first_name and last_name

customer['name'] = customer['first_name']+ " " + customer['last_name']

#customer.drop(columns=['name'], inplace=True) --( How to drop the columns)

customer.cst_marital_status.unique()

customer['marital_status']= customer.cst_marital_status.str.strip().replace({'M':'Married','S':'Single', np.nan : 'n/a'})

customer.cst_gndr.unique()

customer['gender1']= customer.cst_gndr.str.strip().replace({'M':'Male', 'F':'Female', np.nan : 'n/a'})

# customer.drop(columns=['gender'], inplace = True)


customer.to_csv(r'D:\Downloads\data_analytics_data\cust_info_c', index=None)

########################################################################################################################
Merging the columns
########################################################################################################################

cust_az = pd.read_csv(r"D:\Downloads\data_analytics_data\cust_az12_c.csv")

loc_a101 = pd.read_csv(r"D:\Downloads\data_analytics_data\loc_a101_c.csv")

How to merge the tables into one 

customer.columns

cust_az.columns

loc_a101.columns

# loc_a101.rename(columns={'cust_id':'cst_key'}, inplace=True)

# cust_az.rename(columns={'cust_id':'cst_key'}, inplace = True)

customer_final = (

customer[['cst_key', 'name','marital_status', 'gender1']]
.merge(
    cust_az[['cst_key', 'birthdate', 'gender']],
    on='cst_key',
    how='left'
)
.merge(
    loc_a101[['cst_key', 'country']],
    on = 'cst_key',
    how='left'
)

)

customer_final

customer_final['gender_o']= customer_final.gender.replace(np.nan,'n/a')

customer_final.drop(columns=['gender'], inplace=True)

customer_final.loc[customer_final['gender1']=='n/a', 'gender1'] = customer_final.gender_o

customer_final[customer_final['gender1']=='n/a']['gender1']

customer_final.gender1.unique()

customer_final.drop(columns=['gender_o'], inplace=True)

customer_final

customer_final.to_csv(r'D:\Downloads\data_analytics_data\customer_final.csv', index=None)






