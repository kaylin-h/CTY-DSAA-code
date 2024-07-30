from sorting_utilities import *
#from selection_sort import selection_sort

def combine_sorted(array1, array2):
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
        while index2 < len(array2):
            array3[index3] = array2[index2]
            index2 += 1
            index3 += 1

    print(array3)

    #while loop2 to copy left over from array2 if any


a1 = [0, 2, 6, 9, 15]
b1 = [1, 5, 10, 16, 21, 23, 30]
#a1 = generate_array_between(7, 0, 40)
#b1 = generate_array_between(15, 0, 99)
#selection_sort(a1)
#selection_sort(b1)
print(a1)
print(b1)

combine_sorted(a1, b1)