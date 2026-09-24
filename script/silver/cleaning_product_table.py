import pandas as pd
import numpy as np

products = pd.read_csv(r"D:\SQL resource\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\prd_info.csv")

category = pd.read_csv(r"D:\SQL resource\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_erp\PX_CAT_G1V2.csv")

products

categories = category.copy()

categories

products.columns

products[products.prd_key.isnull()]

products.prd_key.str[0:5].replace('-','_')

products['ID']= products['prd_key'].str.split("-").str[0:2].str.join("_")

product = products.copy()

product

product[product.prd_nm.isnull()]

product['prd_start_dt']= pd.to_datetime(product.prd_start_dt)
product['prd_end_dt']=pd.to_datetime(product.prd_end_dt)

product.dtypes

product = product.sort_values(by=['prd_key', 'prd_start_dt'])

product

lead_start_dt = product.groupby('prd_key')['prd_start_dt'].shift(-1)

date_minus_one = lead_start_dt - pd.Timedelta(days=1)

product['end_date'] = date_minus_one

product[['prd_key','prd_start_dt', 'end_date']].head(20)

product[product.prd_cost.isna()]

product.prd_line.unique()

product['product_line']= product.prd_line.str.strip().replace({'M':'Mountain','R':'River','S':'Sea','T':'Tree',np.nan:'n/a'})

product.product_line.unique()

categories.CAT.unique()

categories[categories.ID == categories.ID.str.split()]

categories[categories.SUBCAT.isnull()]

# Merging the table

product.columns

categories.columns

Product_final = product[['ID','prd_nm','prd_cost','product_line','prd_start_dt','end_date' ]].merge(

    categories[['ID','CAT','SUBCAT','MAINTENANCE']],
    on = 'ID',
    how = 'left'
)

Product_final

# Loading into CSV file 

Product_final.to_csv(r"D:\Downloads\data_analytics_data\product_final.csv", index = None)


