

from sorting_utilities import *


def merge_sort(array, begin, end):
    if begin >= end:
        return
    mid = (begin + end)//2
    merge_sort(array, begin, mid)
    merge_sort(array, mid + 1, end )
    merge(array, begin, mid, end)

def merge(array, begin, mid, end):
    array1_size = mid - begin + 1
    array2_size = end - mid

    array1 = [0] * array1_size
    array2 = [0] * array2_size

    for i in range(array1_size):
        array1[i] = array[begin + i]

    for j in range(array2_size):
        array1[j] = array[mid+1+j]

    array3_size = array1 + array2
    array3 = [0] * array3_size
    index1 = 0
    index2 = 0
    index3= 0 #for the bigger array
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] <= array2[index2]:
            array3[index3] = array1[index1]
            index1 += 1
        else:
            array3[index3] = array2[index2]
            index2 += 1
        index3 += 1


        #while loop1 to copy left over from array1 if any
    while index1 < len(array1):
        array3[index3] = array1[index1]
        index1 += 1
        index3 += 1

    #while loop1 to copy left over from array1 if any
    
    while index2 < len(array2):
        array3[index3] = array2[index2]
        index2 += 1
        index3 += 1

    return(array3)

    


a1 = [1, 23, 15, 16, 3, 11]
print(a1)
merge_sort(a1, 0, len(a1)-1)
print(a1)