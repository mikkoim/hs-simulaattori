# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:13:27 2017

@author: Mikko
"""
import os

#path = "C:\\Users\\Mikko\\Google Drive\\koodia\\data\\"
#path = "D:\\Libraries\\Documents\\Mikko\\HS_otsikot\\data1\\"


def read_headers(path):
    dirlist = os.listdir(path)
    
    #header collection to array
    headers = []
    
    #iterate through the directory
    for filename in dirlist:
        
        #match only .txt files
        if filename[len(filename)-4:len(filename)] == ".txt":
            
            #open the .txt -files and save the titles in an array 'otsikot'
            
            try:
                with open(path + filename, 'r', encoding = 'utf-8') as file:
                    o_i = 0
                    otsikot = []
                    otsikko = file.readline()
                    o_i += 1
                    
                    #collect only headers
                    while otsikko != '\n':
                        
                        #don't collect single word headers
                        if len(otsikko.split(' ')) > 2:
                            
                            #some headers have a leading space, remove it
                            if otsikko[0] == ' ':
                                otsikko = otsikko[1:]
                                
                            otsikko = otsikko.replace('\n','')
                            otsikko = otsikko.replace('\ufeff','')
                            otsikot.append(otsikko)
                            
                        otsikko = file.readline()
                        o_i += 1
                        
                    headers.append(otsikot)
                    file.close()
                    
            except UnicodeDecodeError as e:
                print(filename, o_i)
                raise e
                
    o = list(set([j for i in headers for j in i]))
    
    return o, headers