import pandas as pd

data=pd.read_csv('data.csv')

for ind in data.index:
    print(data['FIS'][ind])