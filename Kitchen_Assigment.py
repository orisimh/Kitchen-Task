# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:05:08 2021

@author: User
"""

import pandas as pd
import numpy as np
import operator



# =============================================================================
# this function get the name of the file that include the floor plan 
# the function create a map dataframe of the floor paln by pandas
# =============================================================================
        
def makeAmap(file_name):
    array =[] 
    with open(file_name , 'r') as f: # better way to open file   
        for line in f: # for each line
            out = [line[i:i+1] for i in range(0, len(line)-1)]
            array.append(out)
    
          
    print(array)    
    mp = pd.DataFrame(array)
    return mp 

# =============================================================================
# this function get the map 
# the function find the locations of the employees in the map
# =============================================================================
        
def findtheemployees( mp ):
    
    employees = []
    for  i in range (1,mp.shape[0]) :
       for  j in range (1,mp.shape[1]) :
        
          if(mp.iloc[i,j] ==  'E' ):
               employees.append((i,j))           
    return employees  



# =============================================================================
# this function find the shortest path between employee and certain empty space 
# the path is calculated by BFS Algorithm       
# =============================================================================
        
def FindMinDis(emly ,  x , y , mp ):
    
    # empty data frame of boolean 
    IsVisited = pd.DataFrame( np.empty(shape = [mp.shape[0],mp.shape[1]] , dtype = bool) )
    i = 0
    j=0
    source = (x,y,0)
    while ( i < mp.shape[0]) :
        while ( j < mp.shape[1] ) :
            
            if (mp.iloc[i , j] == 'W'):  # mark Walls as True
                IsVisited.iloc[i, j] = True
            else:
                IsVisited.iloc[i ,j] = False
                
            j= j+1 
        
        i = i+1 
        j=0
 
    
    # start the BFS algorithm 
    queue= [];  # empty queue
    queue.append(source);
    IsVisited.iloc[source[0] ,source[1] ] = True 
    
    while ( len(queue) > 0) :
        current = queue[0];
        queue.pop(0);
        
        
        # if the Destination is reached 
        if (current[0] == emly[0] and current[1] == emly[1]):
            return current[2] 
 
        # the upper node 
        if (current[0] - 1 >= 0 and IsVisited.iloc[current[0] - 1 , current[1]] == False) :
            queue.append((current[0] - 1, current[1] , current[2] + 1))
            IsVisited.iloc[current[0] - 1 , current[1]] = True
        
 
      # the  bottom node 
        if (current[0] + 1 <  mp.shape[0]  and IsVisited.iloc[current[0] + 1 , current[1]] == False) :
            queue.append((current[0] + 1, current[1] , current[2] + 1))
            IsVisited.iloc[current[0] + 1 , current[1]] = True
    
 
       # the left node
        if (current[1] - 1 >=0    and IsVisited.iloc[current[0]  , current[1] -1 ] == False) :
            
            queue.append( (current[0] , current[1] -1  , current[2] + 1))
            IsVisited.iloc[current[0] , current[1]-1]  = True
    
 
 
   # the right node 
        if (current[1] + 1 < mp.shape[1]  and IsVisited.iloc[ current[0] , current[1] + 1 ] == False) :
            
            queue.append( (current[0] , current[1] + 1  , current[2] + 1))
            IsVisited.iloc[current[0] , current[1]+1]  = True

    return -1



# =============================================================================
# this function get the employees locations and the map 
# the function calculate the best location for the kitchen      
# =============================================================================
        
def findTheBestKitchenLocation(employees , mp ):
    i=0 
    j=0 
    dc = {}
    while ( i < mp.shape[0]) :
        while ( j < mp.shape[1] ) :
            
            if (mp.iloc[i , j] == ' '):
                dc[(i,j)]= 0
                for emp_inx in employees:
                  mindis = FindMinDis(emp_inx,i,j ,mp)
                  if(mindis != -1):
                   dc[(i,j)]= mindis + dc[(i,j)]
                  else:
                      dc[(i,j)] = -1
                      break
                  
            j= j+1 
        
        i = i+1 
        j=0
    
    sorted_lc = sorted(dc.items(), key=operator.itemgetter(1))
    # check If the floor plan does not allow for a kitchen
    sumdis = 0
    for loc in sorted_lc:
        
        sumdis =  sumdis + loc[1]
        
    if (len(sorted_lc) == -1*sumdis):
        return -1
    else:
        
        sorted_lc = filter(lambda x: x[1]!= -1 , sorted_lc)
        print(sorted_lc)
        sorted_lc.sort(key=lambda x:x[1])
        return sorted_lc[0][0] 

# =============================================================================

mp =makeAmap('map.txt') 
employees = findtheemployees(mp)          

location = findTheBestKitchenLocation(employees , mp)
if(location != -1):
    print("the recommended location for the kitchen is: {} ".format(location))
else:
    print("the floor plan does not allow for a kitchen")

