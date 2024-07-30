import time
from sorting_utilities import generate_array_between

num_list = generate_array_between(100, 0, 100)
print("before sorting: ", num_list)


def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        temp = num_list[i]
        j = i -1
        while j>=0 and temp < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = temp

''''
for i in range(1, len(num_list)):
    temp = num_list[i]
    for j in range(i-1, -1, -1):
        if temp < num_list[j]:
            num_list[j+1] = num_list[j]
    num_list[j+1] = temp
'''



t1 = time.time_ns()
insertion_sort(num_list)
t2 = time.time_ns()
duration = t2 - t1

print("after sorting: ", num_list)
print("insertion sort took: ", duration, " nanoseconds")