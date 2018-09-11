import pandas as pd
import math
import numpy as np

dfOriginal=pd.read_csv("180801_sales_sic3.csv")
# dfOriginal=pd.read_csv("180801_sales_sic3.csv").drop_duplicates(subset=['gvkey'],keep='first')
dfDes = dfOriginal.groupby(['fyear', 'sic3']).agg({'sale': 'sum'}).reset_index()
# dfOriginal.to_csv('temp.csv')

df1=pd.merge(dfOriginal,dfDes,how='left',on=['fyear','sic3'])
df1['fraction']=df1['sale_x']/df1['sale_y']
df1['squared_fraction']=df1['fraction']*df1['fraction']
df1['squared_fraction_minus']=1-df1['squared_fraction']
df1.to_csv('df1.csv')

# dfResult=df1.drop_duplicates(subset=['gvkey', 'conm'], keep="first")
dfResult=df1.groupby(['gvkey','fyear'])['squared_fraction_minus'].first().unstack().reset_index()
df2=df1.drop('sale_x',1).drop('sale_y',1).drop('fraction',1).drop('squared_fraction',1).drop('fyear',1).reset_index()
df2=df2.drop_duplicates(subset=['gvkey'], keep="first")
# dfResult2=pd.merge(dfResult,df2,on=['gvkey'],how='left').drop('squared_fraction_minus',1)
dfResult2=pd.merge(df2,dfResult,on=['gvkey'],how='right').drop('squared_fraction_minus',1).drop('index',1)
dfResult2.to_csv('dfResult_sic3.csv')
