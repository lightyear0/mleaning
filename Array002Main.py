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
    


'''

Using multimap to print all subarrays

 

We can use multimap to print all sub-arrays with 0 sum present in the given array. The idea is to create an empty multi-map 
to store ending index of all sub-arrays having given sum. We traverse the given array, and maintain sum of elements seen so far. 
If sum is seen before, there exists at-least one sub-array with 0 sum which ends at current index and we print all such sub-arrays.

'''
