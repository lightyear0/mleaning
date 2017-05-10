'''
Created on May 10, 2017

@author: ndharmalingam
'''

'''
Sort binary array in linear time
Given an binary array, sort it in linear time and constant space. Output should print contain all zeroes followed by all ones.


For example,

Input: { 1, 0, 1, 0, 1, 0, 0, 1 }
Output: { 0, 0, 0, 0, 1, 1, 1, 1 }
'''

arr = [ 0, 0, 1, 0,1, 1, 0, 1, 0, 0 ]
a_len = len(arr)
zero_count = 0
for i in arr:
    if i == 0:
        zero_count += 1
        
arr = []

for _ in range(zero_count):
    arr.append(0)
    
for _ in range(a_len-zero_count):
    arr.append(1)
    
print (arr)