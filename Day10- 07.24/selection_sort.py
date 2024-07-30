import time
from sorting_utilities import generate_array_between

num_list = generate_array_between(100, 0, 100)
print("before sorting: ", num_list)

def selection_sort(num_list):
    for i in range(len(num_list)):
        smallest_index = i
        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[smallest_index]:
                smallest_index = j
        temp = num_list[smallest_index]
        num_list[smallest_index] = num_list[i]
        num_list[i] = temp

    

t1 = time.time_ns()
selection_sort(num_list)

t2 = time.time_ns()

duration = t2 - t1

print("after sorting: ", num_list)
print("selection sort took: ", duration, " nanoseconds")