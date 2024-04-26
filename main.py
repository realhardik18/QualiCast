import pandas as pd
from helpers import match_NRR,score

teams_NRR={
    #format:scored,played,conceeded,bowled
    'SRH':[0,0,0,0],
    'PBKS':[0,0,0,0],
    'RR':[0,0,0,0],
    'DC':[0,0,0],
    'RCB':[0,0,0,0],
    'MI':[0,0,0,0], 
    'KKR':[0,0,0,0],
    'GT':[0,0,0,0],
    'CSK':[0,0,0,0],
    'LSG':[0,0,0,0],
}
data=pd.read_csv('data.csv')

for ind in data.index:
    teams=[data['BF'][ind],data['BS'][ind]]
    WT=data['WT'][ind]
    del teams[teams.index(WT)]
    LT=teams[0]
    teams_NRR['BF'][0]+=score(data['BF'][ind])



print(teams_NRR)