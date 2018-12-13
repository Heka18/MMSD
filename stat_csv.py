# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:10:41 2018

@author: jacop
"""
import csv
import numpy as np
import pandas as pd

    
def read_csv1(filename):	
    file = open(filename, "r")
    reader = csv.reader(file, delimiter=",")
    
    x = list(reader)
    return np.array(x);
    
def temp():
    a = pd.read_csv("sdo.csv", low_memory=False) 
    b=0
    it=0
    c=a.as_matrix()
    while(it<554192):
        if(c[it,35]!=c[it,37]):
           b=b+1
        it=it+1
    print(b)
    
    
def readcsv(filename):
    return pd.read_csv(filename, low_memory=False) 
    #return a.as_matrix()
#    return pd.DataFrame(a)
    

def sdo_analisi(filename):
    #anno= "02-01-2012-30-12-2012"
    #filename="sdopiccolo.csv"
    #os.chdir("/Users/stevi/Desktop/MMSD/extraction-05-04-2017/"+anno)
    a= pd.read_csv(filename, low_memory=False)
    fl= pd.DataFrame(a)
    
#    rows = fl.shape[0] 
#    coloumns = fl.shape[1]
    
    newmatrix=pd.DataFrame()
    
    i=0
    j=0
    death = 0
    birth = 0
    other = 0
    ambulance = 0
    direct = 0
    ad=0
    
    while(i<len(fl)):
        if(fl.loc[i][35]!=fl.loc[i][37]):
            newmatrix = newmatrix.append(fl.iloc[j]) 
            j=j+1

            if(fl.loc[i][30]== 'Privata'):
                ad=ad+1
            if(fl.loc[i][5] == 'deceduto'):
                death = death + 1
            elif(fl.loc[i][4] == 'nuovo nato'):
                birth = birth + 1
            elif(fl.loc[i][4] == 'pervenuto tramite  118'):
                ambulance = ambulance + 1
            elif(fl.loc[i][4] == 'altro'):
                other = other + 1
            else:
                direct = direct + 1
        i=i+1
        
    print('Deceduto= '+str(death))
    print('Nato= '+str(birth))
    print('Pervenuto= '+str(ambulance))
    print('Altro= '+str(other))
    print('Generico= '+str(direct))
    print('Privata= '+str(ad))
    newmatrix.to_csv(r'/Users/stevi/Desktop/MMSD/extraction-05-04-2017/31-12-2012-29-12-2013/specdiverse.txt', header=None, index=None, sep=' ', mode='a')    
    return newmatrix



def split_list_csv(filename):
    a = pd.read_csv(filename)
    fl = pd.DataFrame(a)
    dl = pd.DataFrame(a)
    #matrix = [[[0 for _ in range(len(fl))] for _ in range(len(fl.columns)**len(fl.columns))]]
    #newmatrix = np.zeros((len(fl.columns),16))
    
    i = 0
    #tmp_sum = 0
    
    while(i<len(fl)):
        j = 1
        while(j<len(fl.columns)):
#            newList = pd.DataFrame(fl.loc[i][j].split('_'))
            dl.loc[i][j] = fl.loc[i][j].split('_')
#            l = fl.loc[i][j].split('_')
#            week = 0
#            while(week < 16):
#                tmp_sum = tmp_sum + l[weel]
#                newmatrix[i][week] = tmp_sum
#                week = week + 1
            #print(newList)
#            k = 0
#            while(k<len(newList)):
#                dl = dl.append(newList.loc[k][0])
##            print(newList)
#            
#            k = 0
#            print(len(dl.columns))
#            while(k<len(newList)):
#                dl.loc[i][k] = newList.loc[k][0]
#                #dl = dl.append(elem)
#                #print(elem)
#                #matrix[i][k] = elem
#                k = k + 1
            j = j+1
        i=i+1
    return dl

def read_list(row,col,df):
    return df.loc[row][col]

#def total_week(col,df):
#    l = read_list(0,col,df)
#    i = 1
#    while(i < len(df)):
#        df_list = read_list(i,col,df)
#        j = 0
#        while(j < len(df_list)):
#            l[j] = l[j] + df_list[j]
#            j = j + 1
#        
#        i = i + 1
#    
#    return l

def lists_total_week(filename):
    df = pd.DataFrame(split_list_csv(filename))
    j = 1
    #data_frame = pd.DataFrame(df)
    listoflist = []
    
    while(j < len(df.columns)):
        l = read_list(0,j,df)
        i = 1
        while(i < len(df)):
            df_list = read_list(i,j,df)
            k = 0
            while(k < len(df_list)):
                l[k] = l[k] + df_list[k]
                k = k + 1
            i = i + 1
        #df.loc[0][j] = list(l)
        listoflist.append(list(l))
        j = j + 1
    
    #return df
    return listoflist
        
    
            
    
    


#def load_data(filename):
#    csv_database = create_engine('sqlite:///csv_database.db')
#    
#    chunksize = 100000
#    i = 0
#    j = 1
#    for df in pd.read_csv(filename, chunksize=chunksize, iterator=True):
#          df = df.rename(columns={c: c.replace(' ', '_') for c in df.columns}) 
#          df.index += j
#          i+=1
#          df.to_sql('table', csv_database, if_exists='append')
#          j = df.index[-1] + 1
        
#def filetoexcell(filename):
#    # Create a Pandas dataframe from the data.
#    #df = pd.DataFrame(readcsv(filename), columns=('anno','mese','trimestre','n_record','provenienza_assistito','mod_dimissione','data_dimissione','n_gg_presenza','prolungamento_degenza','data_prenotazione','data_ricovero','eta','fascia_eta','mobilita_sdo','mob_attiva_passiva','gg_degenza'))
#
#    df = pd.DataFrame()
#    
#    # Create a Pandas Excel writer using XlsxWriter as the engine.
#    writer = pd.ExcelWriter('dati.xlsx', engine='xlsxwriter')
#    
#    # Convert the dataframe to an XlsxWriter Excel object.
#    df.to_excel(writer, sheet_name='Sheet1')
#    
#    # Close the Pandas Excel writer and output the Excel file.
#    writer.save()