from sorting_utilities import *
#from selection_sort import selection_sort
import time
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        array1 = array[:mid]
        array2 = array[mid:]
        sorted_array1 = merge_sort(array1)
        sorted_array2 = merge_sort(array2)
        full_sorted = merge(sorted_array1, sorted_array2)
        return full_sorted


def merge(array1, array2):
    array3_size = len(array1) + len(array2)
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

    if index1 < len(array1):
        # left over from array1

        #while loop1 to copy left over from array1 if any
        while index1 < len(array1):
            array3[index3] = array1[index1]
            index1 += 1
            index3 += 1

    elif index2 < len(array2):
        # left over from array2

        #while loop2 to copy left over from array2 if any
        while index2 < len(array2):
            array3[index3] = array2[index2]
            index2 += 1
            index3 += 1

    return array3

    


array = generate_array_between(1000000, 0, 100)
print("before sorted: ", array)
t1 = time.time_ns()
sorted_array = merge_sort(array)
t2 = time.time_ns()
duration = t2-t1



print("after sorted: ", sorted_array)
print("merge sort took: ", duration, " nanoseconds")