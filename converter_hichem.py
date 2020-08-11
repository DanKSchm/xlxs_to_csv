import pandas as pd

df = pd.read_xls('./file.xls')
df.to_csv('./file.csv')