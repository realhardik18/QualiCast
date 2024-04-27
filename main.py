import pandas as pd
import json

def Update_Data():
    data=pd.read_csv('data.csv')
    for ind in data.index:
        with open('nrr.json','r') as file:
            data=json.load(file)
        data['RCB']['runs_in']=10
        with open('nrr.json', 'w') as file:
            json.dump(data, file,indent=4)
    
def Overwrite_JSON(team,RIF,OIF,RIS,OIS):
    with open('nrr.json','r'):
        data=json.load(file)

    data[team]['runs_in']+=RIF
    data[team]['runs_out']+=OIF
    data[team]['overs_in']+=RIS
    data[team]['overs_out']+=OIS

    with open('nrr.json', 'w') as file:
            json.dump(data, file,indent=4)
def get_overs(overs):
    if str(overs)==2:
        return float(overs)
    else:
        return float(str(overs).split('.')[0])+float(str(overs).split('.')[-1]/6)

     
#Update_Data()
print(get_overs('20'))