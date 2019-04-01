# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 00:38:23 2019

@author:Devavrat+SVR+ShareMarket
By Siraj Raval
Step 1: Import CSV ,numpy,SVP,pyplot
Step 2:need dates and prices from files as an array
Step 3: Need a model
Step 4: Prediction
Step 5: Plotting Dates
"""

import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
dates=[]
prices=[]

with open('HistoricalQuotes.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)
    for lines in csv_reader:
        dates.append(int(lines[0].split('/')[1]))
        prices.append(float(lines[1]))

x=np.array(dates)
y=np.array(prices)
x=x.reshape(-1,1)

         
clf= SVR(kernel='linear',C=1e3,gamma=0.1)
clf.fit(x,y)

prize=clf.predict(x)
print(prize)
plt.scatter(prices,x,color='black')
#plt.plot(prize,x)



#hence rbf is most fitting