# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:41:33 2023

@author:WANG Phoenix, Deparment of Mechanical Engineering, THE HONG KONG POLYTECHNIC UNIVERSITY
C
"""
import pandas as pd
import numpy as np
from collections import Counter

path = './table.csv'
table = pd.read_csv(path)
table = table.fillna(value = 'Z')

diction = {'A':10000,
           'E':1000,
           'I':100,
           'O':10,
           'U':1,
           'X':-10000,
           'Z':0}



def TCR_calculation(table,TCR):
    
    for i in range(len(table)):
        TCR_value = 0
        temp = table.loc[i,:]
        counting = Counter(temp)
        
        for count in counting:
            TCR_value = TCR_value + abs(counting[count]*diction[count])
        
        TCR.append(TCR_value)
        

def sequence_generation(table,TCR,diction):
    
    start_pos = TCR.index(max(TCR))
    sequence = [start_pos+1]
    #counting = 0
    history = [start_pos]
    temp = table.loc[start_pos,:]
    countA = list(Counter(temp))
    countA.sort()
    for count in countA:
        if count == 'Z':
            break
        judge_container = []
            
        for i in range(len(temp)):
            if temp[i] == count:
                if i not in history:
                    judge_container.append(i)
            
        if len(judge_container)==1:
            
            sequence.append(judge_container[0]+1)
            history.append(judge_container[0])
            
        else:
            
            dictionary = {}
            
            for j in judge_container:
                dictionary[str(j)] = TCR[j]
                history.append(j)
                
            dictionary = sorted(dictionary.items(),key=lambda x:-x[1])
            
            for j in dictionary:
                sequence.append(int(j[0])+1)
            
        
        
    return sequence



TCR = []
TCR_calculation(table, TCR)

seq = sequence_generation(table, TCR, diction)

    
