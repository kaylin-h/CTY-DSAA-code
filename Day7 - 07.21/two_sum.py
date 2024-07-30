numbers_list = [1, 0, 3, -4, 9, 31, -21]
target = 10
numbers_list.sort()
for x in range(0, len(numbers_list)-1):
    for y in range(x+1, len(numbers_list)):
        if numbers_list[x] + numbers_list[y] == target:
            print(numbers_list[x], " and ", numbers_list[y], " add up to", target)




