'''
Created on May 10, 2017

@author: ndharmalingam
'''
'''
Print all sub-array with 0 sum
Given an array of integers, print all subarrays having 0 sum.

 


For example,

Input:  { 4, 2, -3, -1, 0, 4 }

Sub-arrays with 0 sum are

{ -3, -1, 0, 4 }
{ 0 }
 

Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

Sub-arrays with 0 sum are

{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

'''

from collections import defaultdict
table = defaultdict(list)

arr = [ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ]
 
table[0].append(-1)
pos = 0
n_sum = 5
for  num in  arr:
    n_sum += num
    if table.get(n_sum) != n_sum:
        for item in table[n_sum]:
            print(item+1,' .. ',pos)
    table[n_sum].append( pos)
    pos += 1
    

