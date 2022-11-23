import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv("D:\pythonProject\pr3\Avocado.csv", delimiter=',')
print(df)
print('------------------------info------------------------------')
print(df.info())
print('------------------------head------------------------------')
print(df.head())
print('------------------------isna------------------------------')
print(df.isna().sum())
