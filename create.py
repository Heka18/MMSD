#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:35:41 2018

@author: stevi
"""
import pickle
import os
import numpy as np
import csv
import pandas as pd 



#yep
def readcsv(filename):
    return pd.read_csv(filename, low_memory=False) 


def get_all_dataSet():
    owd= os.getcwd()
    os.chdir(owd+"/dataSet/")
    dataset_list=[]
    for file in glob.glob('*.txt'):
        dataset_list.append(file)
    return dataset_list

def find_sentiment(file):
    return file[8:-4]

def falstart():
    count = 0
    startDir=os.getcwd()
    lexical_resources = labDBSA.get_lexical_resources()
    collection = open_connection_to_mongo()
            
    dataset_list=get_all_dataSet()
    owd= os.getcwd()
    parentDir=os.path.abspath(os.path.join(owd, os.pardir))
    
    for file in dataset_list :    
        with open(file, 'r', encoding='utf-8') as myfile:
            data=myfile.read().replace('\n', '')
            wordsFiltered = labDBSA.run_clean_tweet(data,parentDir)
            words_dict = labDBSA.createDictionary(wordsFiltered,lexical_resources)
            #caricamento su Oracle
            oracleDB.connessioneOracle(words_dict,wordsFiltered,file)
            #caricamento su Mongo
            count = mongoDB.caricamentoMongo(wordsFiltered,file,count,collection)
            os.chdir(startDir)       
            sentiment=find_sentiment(file)
            wordsCloud.create_word_cloud(sentiment,wordsFiltered)
            os.chdir("/Users/stevi/.spyder-py3/ProgettoLabDB/dataSet/")

    mongoDB.mapReduce(collection)

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def filldict():
    hospital_dict= dict()
    spec_dict= dict()
    week_dict= dict()
    hospital_dict[id_hospital]= spec_dict
    spec_dict[id_spec]= week_dict
    week_dict[week_num]= num_patients

def is_not_empty(patients_array):
    c=0
    while(c<len(patients_array)):
        if(patients_array[0] != 0):
            return True
        c=c+1
    
    return False
        
    
# Ritorna un array di int che corrispondono al numero di pazienti in quella settimana(es. indice 1 value 3= 3 pazienti nella seconda settimana)
def parse_cel(df,riga,c):
    separator=['_']
    patients_array=[int(h) for h in df.loc[riga][c] if h not in separator]
    
    return patients_array

def create_week_dict(df,riga,c):
    week_dict= dict()
    patients_array=parse_cel(df,riga,c)
    w=0
    if(is_not_empty(patients_array)):
        while(w<52):
            week_dict[w+1]=patients_array[w]    
            w=w+1
    
    return week_dict
        
def create_hospital_dict(id_hosp,df,riga,columns,columns_values):
    spec_dict= dict()
    c=1
    
    while(c<columns):
        id_spec= columns_values[c]
        c_w_d= create_week_dict(df,riga,c)
        if(bool(c_w_d)):
            spec_dict[id_spec]= c_w_d
        c=c+1
    
    return spec_dict

#liste di dizionari [{id_osp1:[{id_spec:{num_week:#_patients}}]}]
def start(filecsv):
    filename= pd.read_csv(filecsv, low_memory=False)
    df= pd.DataFrame(filename)
    
    riga=0
    num_week=0
    columns = df.shape[1]
    
    file_dict= dict()
    columns_values=list(df)
    
    
    while(riga<len(df)):
        id_hosp = df.loc[riga][0]
        file_dict[id_hosp]= create_hospital_dict(id_hosp,df,riga,columns,columns_values)
        riga= riga+1
        
    

    return file_dict   
        

def quick_start(filecsv):
    filename= pd.read_csv(filecsv, low_memory=False)
    df= pd.DataFrame(filename)
    
    a=parse_cel(df,1,1)
    return a
    
    
    
    
    
    
    
    
    
    
    
    
    
    