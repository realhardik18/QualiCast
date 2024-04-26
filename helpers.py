def match_NRR(s1,s2):
    RR1=team_RR(s1)
    RR2=team_RR(s2)
    return round(RR1-RR2,4)

def team_RR(score):
    score=score.replace(' ','').split(',')
    score[-1]=score[-1][1:-1].replace('ov','')
    if len(score[-1])!=2:
        ov,b=score[-1].split('.')
        score[-1]=float(ov)+float(b)/6
    else:
        score[-1]=int(score[-1])
    score[0]=int(score[0].split('/')[0])
    return round(score[0]/score[-1],4)

def score(data):
    score=data.replace(' ','')
    return int(score.split('/')[0])

#print(score(" 224/4"))
#print(team_RR(' 287/4, (50 ov) '))
#print(match_NRR(' 287/4, (50 ov) ',' 243/4, (50 ov) '))