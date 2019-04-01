# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 00:26:40 2019

@author: Devavrat+LightFM
"""

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#here we will fetch the movies with the function fetch_movielens
data=fetch_movielens(min_rating=4.0)


print(repr(data["test"]))

model=LightFM(loss='logistic')
model.fit(data['train'],epochs=30,num_threads=2)

from lightfm.evaluation import precision_at_k
print("precision of test %.2f" %precision_at_k(model,data['test'],k=5).mean())
print("precision of train %.2f" %precision_at_k(model,data['train'],k=5).mean())

def sample_recc(model,data,user_ids):
    n_users,n_items=data['train'].shape  #data[].shape returns two values 
    #one for n_users and another one for n_items
    
    #for every user we will print the top 3 movies
    for user_id in user_ids:
        known_positives=data['item_labels'][data['train'].tocsr()[user_id].indices]
        #here we first take data, than we go to the row item_labels, than we need to know on which index
        #we should go for taking items or movie names. for that
        #we take the train as coo_matrices convert that to csr so that we can use the indexing feature 
        #now we can find any user as data['train'].tocsr()['user indexing']
        #now we just need indexing so use indices
        #data['train'].tocsr()[user_id].indices by this we got the array of indices
        
        #now we will predict the recommandations based on our trained models
        scores=model.predict(user_id,np.arange(n_items)) #calculate the scores
        
        #we got the rating , now we will sort it from high value to low
        top_items=data['item_labels'][np.argsort(-scores)] #negative because high to low
        
        #now we will  print the known as well as predicted values
        #remenber both can be same also
        
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)
            
sample_recc(model,data,[3,13,23])

        
        