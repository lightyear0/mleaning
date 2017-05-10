'''
001. Find pair with given sum in the array

Created on May 10, 2017

@author: ndharmalingam
'''
'''
Find pair with given sum in the array
Given an unsorted array of integers, find a pair with given sum in it.

 


For example,

Input:
arr = [8, 7, 2, 5, 3, 1]
sum = 10

Output: 
Pair found at index 0 and 2 (8 + 2)
OR
Pair found at index 1 and 4 (7 + 3)

'''

def findPair(data, sumValue):
    table = {}
    flage = False
    
    for i in range(len(data)):
        if table.get(sumValue - data[i]) != None:
            print(table[sumValue - data[i]], " and ", i)
            flage = True
        table[data[i]] = i
    
    return flage

arr = [1, 2, 5, 8, 9, 1]
sumValue = 10

if findPair(arr, sumValue):
    print('Found Pair')
else:
    print("Not Found Pair")
    
    
'''
O(n) solution using Hashing –

 We can use map to easily solve this problem in linear time. The idea is to insert each element of the array arr[i] in a map. 
 We also checks if difference (arr[i], sum-arr[i]) already exists in the map or not. If the difference is seen before, 
 we print the pair and return
 
'''
