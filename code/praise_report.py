
# coding: utf-8

# In[11]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd


# In[12]:

path = '../data/Report.csv'
report = pd.read_csv(path)
report['MS_Code']=report.Mustard_Seed.map({'Agapao':0,'Ahinsan':1,'Aleph':2, 'Balaal':3, 'Bohyen':4,'Doxa':5,
                                           'El-Zoe':6,'GTUC':7,'Koinonia':8,'Mowed':9,'Oforikrom':10,'Parah':11,
                                           'Sodzo':12})

Mustard_Seeds =['Agapao','Ahinsan','Aleph', 'Balaal', 'Bohyen','Doxa',
                'El-Zoe','GTUC','Koinonia','Mowed','Oforikrom','Parah',
                'Sodzo']
print report.shape
print report.Mustard_Seed.value_counts()
#print report.Date.value_counts()
report.head(2)


# In[13]:

#X_test[(y_pred_class ==1) & (y_test==0)]
Date =  report.Date
MS = report.Mustard_Seed
MSCode = report.MS_Code 
SW = report.Souls_Won
FT = report.Firstimers
TA = report.Total_Attendance
SS = report.SS_Attendance
TO = report.Offertory


# In[14]:

print len(Mustard_Seeds)


# In[30]:

ls = [6,8]
HAT = []
for i in range(len(Mustard_Seeds)):
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
    
X = range(len(Mustard_Seeds))
plt.xticks(X, Mustard_Seeds)
plt.bar(X,HAT)
plt.savefig("../plots/Highest_attendance")


# In[ ]:

#MS.sort_values()


# In[ ]:

print MS[8]


# In[ ]:



#names = ['anne','barbara','cathy']
#counts = [3230,2002,5456]
#pylab.figure(1)
#x = range(3)
#pylab.xticks(x, names)
#pylab.plot(x,counts,"g")
#pylab.show()


# In[ ]:

print report.MS_Code.key(1


# In[ ]:

plt.hist(report.Offertory)


# In[ ]:



