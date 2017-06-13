#! /env/python

# coding: utf-8

# In[31]:

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd


# In[53]:

path = '../data/Report.csv'
report = pd.read_csv(path)
report['MS_Code']=report.Mustard_Seed.map({'Agapao':0,
                                           'Ahinsan':1,
                                           'Aleph':2,
                                           'Balaal':3,
                                           'Bohyen':4,
                                           'Doxa':5,
                                           'El-Zoe':6,
                                           'GTUC':7,
                                           'Koinonia':8,
                                           'Mowed':9,
                                           'Oforikrom':10,
                                           'Parah':11,
                                           'Sodzo':12})

Mustard_Seeds =['Agapao',
                'Ahinsan',
                'Aleph',
                'Balaal',
                'Bohyen',
                'Doxa',
                'El-Zoe',
                'GTUC',
                'Koinonia',
                'Mowed',
                'Oforikrom',
                'Parah',
                'Sodzo']

print report.shape
#print report.Mustard_Seed.value_counts()
#print len(report.Mustard_Seed.keys)
#print report.Date.value_counts()
#report.head(2)
print (len(report.Mustard_Seed.unique()))
lght = report.Mustard_Seed.unique()
print lght
report.Mustard_Seed.unique()


# In[54]:

Date =  report.Date
MS = report.Mustard_Seed
MSCode = report.MS_Code 
SW = report.Souls_Won
FT = report.Firstimers
TA = report.Total_Attendance
SS = report.SS_Attendance
TO = report.Offertory


# In[55]:

ls = [6,8]
HAT = []
for i in range(len(report.Mustard_Seed.unique())-1):
    D1 = Date[MSCode == i]
    TAtt = TA[MSCode == i]
    HAT.append(max(TAtt))
    Fti = FT[MSCode == i]
    #j=ls[i]
    x = range(len(D1))
    plt.xticks(x, D1)
    #plt.subplot(1, 2, j)
    #plt.subplots(1, 2, figsize=(20, 4))
    plt.plot(x,TAtt, marker='o')
    plt.plot(x,Fti,marker='p')
    plt.title(Mustard_Seeds[i])
    plt.legend()
    #plt.ylim(0,100)
    plt.savefig("../plots/"+Mustard_Seeds[i]+str(".png"))
    plt.show()
    
X = range(len(report.Mustard_Seed.unique())-1)
plt.xticks(X, Mustard_Seeds)
plt.bar(X,HAT)
plt.savefig("../plots/Highest_attendance")


# In[ ]:




# In[ ]:




# In[ ]:



