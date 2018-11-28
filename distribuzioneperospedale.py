#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:48:07 2018

@author: stevi
"""

# Matrice ospedale/#settimana dove indichiamo per ogni ospedale quante entrate 
# ha in quella settimana

import os
import pandas as pd
import numpy as np



def start():
    anno= "2011" #"2012"  "2013"
    filename="originToHospitalDistribution.csv"
    os.chdir("/Users/stevi/Desktop/MMSD/dati_elaborati/"+anno)
    a= pd.read_csv(filename, low_memory=False)
    fl= pd.DataFrame(a) # matrice del file
    rows = fl.shape[0] # numero di righe
    coloumns = fl.shape[1]
    
    #newmatrix = np.matrix()
    #newmatrix=np.full((rows+1,coloumns+1),0)
    #print(rows) #1128
    #print(coloumns) #117
    newmatrix = np.zeros((coloumns,52))
    #print(newmatrix)
    #print(fl)
    i=1
    j=1
    week=0
    tmpsum = 0
    
    while(j < coloumns): # ospedali
        #newmatrix[j][0] = fl.iloc[0][j]
        while(week<51):
            while( i < rows): # comuni
                cella=fl.iloc[i][j].split("_")
                tmpsum = tmpsum + int(cella[week]) 
                #print("La somma tmp nella riga ",i," è ",tmpsum)
                i=i+1
            newmatrix[j][week]=tmpsum
            #print("Nella settimana ", week, " ci sono in totale ",tmpsum," persone nell'ospedale ",j)
            #print(newmatrix[j][week])
            week=week+1
            tmpsum=0
        j=j+1
    
    df=pd.DataFrame(newmatrix)
    #df.pd.DataFrame.to_csv("outputhospitalweek.csv")
    return newmatrix

#
def sdoanalisi():
    anno= "02-01-2012-30-12-2012"
    filename="sdopiccolo.csv"
    os.chdir("/Users/stevi/Desktop/MMSD/extraction-05-04-2017/"+anno)
    a= pd.read_csv(filename, low_memory=False)
    fl= pd.DataFrame(a)
    
    rows = fl.shape[0] 
    coloumns = fl.shape[1]
    
    newmatrix=pd.DataFrame()
    
    i=0
    j=0
    
    while(i<len(fl)):
        if(fl.loc[i][35]!=fl.loc[i][37]):
            newmatrix = newmatrix.append(fl.iloc[i]) 
            j=j+1
        i=i+1
    return newmatrix





