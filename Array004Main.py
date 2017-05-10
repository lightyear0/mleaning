'''
Created on May 10, 2017

@author: ndharmalingam
'''

'''
Find a duplicate element in a limited range array
Given a limited range array of size n where array contains elements between 1 to n-1 with one element repeating, find the duplicate number in it.

 


For example,

Input:  { 1, 2, 3, 4, 4 }
Output: The duplicate element is 4
 

Input:  { 1, 2, 3, 4, 2 }
Output: The duplicate element is 2
'''

arr = [ 1, 2, 3, 4, 4]

ret = arr[0]
pos = 1
for i in arr[1:]:
    ret ^= i
    ret ^= pos
    pos +=1
    
print (ret)