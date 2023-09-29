import pandas as pd

pd.set_option('display.max_columns',None)

df=pd.read_csv('sales_data.csv')

df['Category']=df['Category'].replace('Vêtements', 'Clothing')
df['Category']=df['Category'].replace('Électronique', 'Electronics')

print(df.head(10))

print(df.keys())

