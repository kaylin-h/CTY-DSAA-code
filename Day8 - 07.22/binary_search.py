#binary search using recursion
def binary_search(num_list, target,low, high):
    num_list.sort()
    if high < low:
        return -1
       
    mid = ((high + low) // 2)
    print("Index that has been examined:")
    if target == num_list[mid]:
        return mid
    elif target > num_list[mid]:
        print(mid)
        return binary_search(num_list, target, mid+1, high)
    elif target < num_list[mid]:
        print(mid)
        return binary_search(num_list, target, low, mid-1)
    
    
number_list = [1,2,3,4,5,6,7,8,9,10,11]
target = 12

    
answer = binary_search(number_list, target, 0, len(number_list)-1)
print("target is at index: ",answer)




'''
#using a while loop to binary search

while high >= low:
    mid = (high + low) // 2
    if target == number_list[mid]:
        print("target is at index: ", answer)
    elif target >= number_list[mid]:
        low = mid + 1
    else:
        high = mid - 1
print("number was not found")

'''
    
