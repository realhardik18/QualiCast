import pandas as pd
import json

data=pd.read_csv('data.csv')

def Overwrite_JSON(team,RS,RG,OP,OB):
    with open('nrr.json','r') as file:
        data=json.load(file)

    data[team]['runs_scored']=str(RS+int(data[team]['runs_scored']))
    data[team]['runs_given']+=str(RG+int(data[team]['runs_given']))
    data[team]['overs_played']+=str(get_overs(OP)+float(data[team]['overs_played']))
    data[team]['overs_bowled']+=str(get_overs(OB)+float(data[team]['overs_bowled']))

    with open('nrr.json', 'w') as file:
            json.dump(data, file,indent=4)

def get_overs(overs):
        if len(str(overs))==2:
            return float(overs)
        else:
            return float(overs.split('.')[0])+float(overs.split('.')[-1])/6
        
def Update_data():
    for ind in data.index:
        team_1=data['BF'][ind]
        team_2=data['BS'][ind]

        team_1_runs=data['FIS'][ind]
        team_2_runs=data['SIS'][ind]

        team_2_bowled=str(data['O1'][ind])
        team_1_bowled=str(data['O2'][ind])
        #print(type(team_1_bowled))

        Overwrite_JSON(
            team=team_1,
            RS=team_1_runs,
            RG=team_2_runs,
            OP=team_2_bowled,
            OB=team_1_bowled)
        Overwrite_JSON(
            team=team_2,
            RS=team_2_runs,
            RG=team_1_runs,
            OP=team_1_bowled,
            OB=team_2_bowled)
        print(f'written data for match number {ind+1}')

Update_data()

    
#fix overwriting issue        