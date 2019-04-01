# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:30:58 2019

@author: nEW u
"""

from sklearn import neighbors

#height, weight , shoe size
female=1;
male=0;

x=[[181,70,21],[110,55,24],[160,62,25],[130,62,25],[120,63,26],[172,65,23],[140,64,24],[173,35,23],[120,62,22]]

#y=[female,male,female,male,male,female,female,female,male]
#y=['female','male','female','male','male','female','female','female','male']

#clf=tree.DecisionTreeClassifier()   #tree package and DTC class....Here object cretaion is done

#clf=svm.SVC() 

clf=neighbors.KNeighborsClassifier(9)

clf=clf.fit(x,y)       #calling the function which fits the training data
pred=clf.predict([[110,32,73]])

print(pred)



#output on[110,32,73]
#Tree:male
#svm:female
#neighbors: female