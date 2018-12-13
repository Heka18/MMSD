#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:17:26 2018

@author: stevi
"""
import pickle
  
#creazione dell'oggetto pickle
# =============================================================================
# def save_obj(obj, name):
# #    with open('datiStrutturati/'+ name + '.pkl', 'wb') as f:
# #        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
#     f = open('datiStrutturati/' + name + '.pkl', 'rb')  
#     mydict = pickle.dump(f)
#     f.close()   
#     return mydict
# 
# #caricamento dell'oggetto pickle
# def load_obj(name):
# #    with open('datiStrutturati/' + name + '.pkl', 'rb') as f:
# #        return pickle.load(f)
#     f = open('datiStrutturati/' + name + '.pkl', 'rb')  
#     mydict = pickle.load(f)
#     f.close()   
#     return mydict
# =============================================================================


def save_obj(obj, name):
    with open('datiStrutturati/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('datiStrutturati/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)