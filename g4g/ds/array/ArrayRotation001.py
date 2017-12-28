'''
Created on Aug 1, 2017

@author: ndharmalingam

http://www.geeksforgeeks.org/array-rotation/
http://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
http://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/

'''

def swap(arr,start,end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def left_rotate(arr,n):
    swap(arr,0,n-1)
    swap(arr,n, len(arr)-1)
    swap(arr,0,len(arr)-1)


def right_rotate(arr,n):
    swap(arr,n,len(arr)-1)
    swap(arr,0,n-1)
    #swap(arr,0,len(arr)-1)
    
    
arr = [1,2,3,4,5,6,7]
n = 4

print ( "Before : " , arr)

left_rotate(arr,n)

print ( " After : " , arr)



arr2 = [1,2,3,4,5,6,7]
n2 = 2
print ( arr2)
right_rotate(arr2, n2)
print ( arr2)
