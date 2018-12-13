#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:48:07 2018

@author: stevi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:35:41 2018

@author: stevi
"""
import os
import pandas as pd 
import saveLoadObj
import pickle

#se la lista passata ha solo valori nulli ritorno False altrimenti True
def is_not_empty(parsed_array):
    c=0
    length=len(parsed_array)
    
    while(c<length):
        if(parsed_array[c] != 0):
            return True
        c=c+1
    
    return False
        
#Parsifico la cella di riga row e colonna c inserendo i valori in una 
#lista con elementi separatori quelli presenti in separator
def parse_cel(df,row,c):
    parsed_array=[]
    
    if(df.loc[row][c] != " "):
        parsed_array= df.loc[row][c].split("-")
        del parsed_array[-1] #serve perchè alla fine inseriva uno spazio bianco
     
    return parsed_array

#creazione dizionario dei valori delle settimane
def create_list(df,row,c):
    parsed_array=parse_cel(df,row,c)
    
    if(is_not_empty(parsed_array)): 
        return parsed_array            
    
    return []
 
#creo dizionario  delle specialità
def create_second_dict(df,row,number_of_columns,columns_titles):
    second_dict= dict()
    c=1 
    
    while(c<number_of_columns):
        second_key= columns_titles[c]
        temp_spec_list= create_list(df,row,c)
        if(len(temp_spec_list)>0):
            second_dict[second_key]= temp_spec_list
        c=c+1
    
    return second_dict

# Struttura {id_comune:{id_spec:[id_osp]}}
def start(filecsv):
    filename= pd.read_csv(filecsv, low_memory=False)
    df1= pd.DataFrame(filename) 
    df=df1.fillna(" ")

    row=0
    number_of_columns = df.shape[1] #Numero di colonne del file
    print(number_of_columns)
    file_dict= dict()
    columns_titles=list(df) #Titoli delle colonne
    
    length_df= len(df)
    
    while(row<length_df):
        first_key = df.loc[row][0]#Chiave del primo dizionario
        file_dict[first_key]= create_second_dict(df,row,number_of_columns,columns_titles)
        row= row+1
        
    #name_new_file= 'hospitalToSpecialtyDistribution'
    name_new_file=os.path.splitext(filecsv)[0]
    #saveLoadObj.save_obj(file_dict,name_new_file)
    save_obj(file_dict,name_new_file)

    return file_dict   
        


def save_obj(obj, name):
    with open('datiStrutturati/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('datiStrutturati/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
# =============================================================================
# metodo di prova
#  def quick_start(filecsv):
#      filename= pd.read_csv(filecsv, low_memory=False)
#      df= pd.DataFrame(filename)
#      
#      a=parse_cel(df,1,1)
#      return a
# =============================================================================
    
  
    
    
    
    
    
    
    
    
    
    
    
    





