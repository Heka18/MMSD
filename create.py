#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:35:41 2018

@author: stevi
"""
import pickle
import pandas as pd 

def save_obj(obj, name):
    with open('datiStrutturati/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('datiStrutturati/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def is_not_empty(parsed_array):
    c=0
    length=len(parsed_array)
    
    while(c<length):#Controllo se nella lista c'è almeno un valore diverso da 0
        if(parsed_array[c] != 0):
            return True
        c=c+1
    
    return False
        
    
def parse_cel(df,row,c):
    separator=['_']
    #Parsifico la cella di riga row e colonna c inserendo i valori in una 
    #lista con elementi separatori quelli presenti in separator
    parsed_array=[int(h) for h in df.loc[row][c] if h not in separator]
    
    return parsed_array


def create_third_dict(df,row,c):
    third_dict= dict()
    parsed_array=parse_cel(df,row,c)
    w=1 #Numero della settimana
    
    if(is_not_empty(parsed_array)):#Se ha valori utili creo le settimane 
        while(w<53):#52 settimane in un anno
            third_dict[w]=parsed_array[w-1]    
            w=w+1
    
    return third_dict
 
       
def create_second_dict(df,row,number_of_columns,columns_titles):
    second_dict= dict()
    c=1 #Colonna corrente
    
    while(c<number_of_columns):
        second_key= columns_titles[c]
        temp_week_dict= create_third_dict(df,row,c)
        if(bool(temp_week_dict)):#E' falso se il dict è vuoto
            second_dict[second_key]= temp_week_dict
        c=c+1
    
    return second_dict


#dizionario di dizionari {id_osp:{id_spec:{num_week:#_patients}}}
def start(filecsv):
    filename= pd.read_csv(filecsv, low_memory=False)
    df= pd.DataFrame(filename) #Creo il DataFrame del file csv
    
    row=0
    number_of_columns = df.shape[1] #Numero di colonne del file
    
    file_dict= dict()
    columns_titles=list(df) #Titoli delle colonne
    
    length_df= len(df)
    
    while(row<length_df):
        first_key = df.loc[row][0]#Chiave del primo dizionario
        file_dict[first_key]= create_second_dict(df,row,number_of_columns,columns_titles)
        row= row+1
        
    name_new_file= 'hospitalToSpecialtyDistribution'
    save_obj(file_dict,name_new_file)
    return file_dict   
        

# =============================================================================
#  def quick_start(filecsv):
#      filename= pd.read_csv(filecsv, low_memory=False)
#      df= pd.DataFrame(filename)
#      
#      a=parse_cel(df,1,1)
#      return a
# =============================================================================
    
  
    
    
    
    
    
    
    
    
    
    
    
    