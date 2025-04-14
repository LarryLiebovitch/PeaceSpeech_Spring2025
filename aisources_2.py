#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:19:12 2024

@author: larrynl3
TO READ ALL NOW COUNTRIES AND MAKE CSV OF SOURCES AND COUNTS OF EACH
"""
import pandas as pd
import numpy as np
import math
import os

def fileout (filename,filedata):
    f2=open(filename,'w')
    f2.write(filedata)
    f2.close()
    
#read in country abbreviations
AI_2_NOW='/Users/larrynl3/Documents/PROGRAMS/pyzoprograms/AI_2_NOW'
dfcc = pd.read_csv(AI_2_NOW+'/countrycodes.csv')
cname=dfcc['Countryname'].tolist()
c2name=dfcc['2letter'].tolist()
letters_to_names=dict(zip(c2name, cname))

#get ready to read each country file
datapath=AI_2_NOW+'/now'
datadir=dir_list = os.listdir(datapath)
print(datadir)
datadir.pop(0) # to kill the fist '.DS_Store' in dir return
print('\nnow with pop(0)\n',datadir)
ncountry=len(datadir) #NOTE: len(datadir)=len(name_country)+1
print('\nnumber of countries=  ', ncountry)

abreviation_country=[]
name_country=[]
for icountryin in range (0,ncountry):
    next_abbreviation=datadir[icountryin][0:2]
    abreviation_country.append(next_abbreviation)
    # print ('\n',icountryin,next_abbreviation)
    next_name=letters_to_names[next_abbreviation]
    name_country.append(next_name)
    print ('\n abbreviation,name=  ',next_abbreviation,next_name)

# set_name=[]
# cunique_values=np.zeros(ncountry)
# cunique_values = [' ' for _ in cunique_values]
set_name=input ('Please give me a SETNAME, e.g. AA ')
#INITIALIZE COUNTRY START STOPS
# for icountry in range (0,ncountry):
for icountry in range (0,ncountry):
    input_file=AI_2_NOW+'/now/'+datadir[icountry]
    name=name_country[icountry]
    print('\n',icountry,name)
    df=pd.read_csv(input_file)
    # unique_values = df['publisher'].unique()
    # cunique_values[icountry]=unique_values
    unique_counts = df['publisher'].value_counts()
    print(unique_counts)
    dfc=pd.DataFrame(unique_counts)
    outtest=input('Do you want to save publishers this country (y/n), Def.=n ')
    outtest=outtest.lower()
    if outtest == 'y':
        if set_name==[]: 
            set_name=input ('Please give me a SETNAME, e.g. AA ')
        filesources=AI_2_NOW+'/NOW_sources/'+set_name+name+'.csv'
        dfc.to_csv(filesources, sep=',')
        print ('/nfile saved')


    
    
    # # Counting unique values in column 'D'
    # unique_counts = df['D'].value_counts()
    
    # print("Counts of unique values in column 'D':")
    # print(unique_counts)
    
    
# DataFrame.to_csv(filename, sep=',', index=False, encoding='utf-8')
    
    # cwords_row=[]
    # cwords_row_sum=0
    # # result_string=text[cstart]+' '
    # result_string=''
    # total_set_words=nk*nsets
    # for j1 in range(cstart,cend):
    #     new_words=count_words(text[j1])
    #     cwords_row.append(new_words)
    #     cwords_row_sum=cwords_row_sum+new_words
    #     result_string=result_string+text[j1]+' '
    #     set_end=j1
    #     if cwords_row_sum >= total_set_words: break
    # print ('\n',name,'total words this country=  ',cwords_row_sum)
    
    # # country_end=min(nsets,int(words_test/nk))
    # set_end=min(nsets,cwords_row_sum)
    # country_set=[]
    # xx=result_string.split()
    # # for i6 in range(country_end):
    # for i6 in range(set_end):
    #     yy=' '.join(xx[i6*nk:(i6+1)*nk])
    #     country_set.append(yy)
    #     # print ('\ni6, yy',i6,yy) #REMOVED FROM airead_11.py
        
    # outtest=input('Do you want to save thise country to a set of files (y/n), Def.=n ')
    # outtest=outtest.lower()
    # if outtest == 'y':
    #     if set_name==[]: 
    #         set_name=input ('Please give me a SETNAME, e.g. AA ')
    #     for i7 in range(set_end):
    #         if country_set[i7] != '':
    #             filenameout=set_name+'_'+name+'_'+str(i7)
    #             fileout(filenameout,country_set[i7])
    #             print ('\nfile saved')
    