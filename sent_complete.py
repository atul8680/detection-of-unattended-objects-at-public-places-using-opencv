#importing libraries
#import numpy as np
import pandas as pd
import re

#importing data
dataset=pd.read_csv('training.1600000.processed.noemoticon.csv',encoding='cp1252')
data=dataset.iloc[:,-1:].values


wbank=dict()
for k in range(1599999): 
    tweet=re.sub('[^a-zA-Z]',' ',str(data[k,:]))  #cleaning of text
    tweet=tweet.lower()
    words=tweet.split()
    for m in range(1,4):
        if len(words)>=m+1:   
            for i in range(len(words)-m):
                key=[]
                for j in range(m):
                    key.append(words[i+j])  
                key=' '.join(key)
                ans=words[i+m]
                if key in wbank:
                    if ans in wbank[key]:
                        wbank[key][ans]+=1
                    wbank[key][ans]=1
                wbank[key]={}
                wbank[key][ans]=1 

def predict(dic,q):
    q=re.sub('[^a-zA-Z]',' ',q)  #cleaning of text
    q=q.split()
    for x in range(4):
        Q=' '.join(q[x:])
        if Q in dic:
            sentence=sorted(dic[Q].items(), key=lambda x: x[1])
            for n in sentence:
                print(n[0],sep=' ')
                break
    if x==3:
        print('best predicted words')
        return
    print('enter correct words')
    
      
predict(wbank,'i wish to have')