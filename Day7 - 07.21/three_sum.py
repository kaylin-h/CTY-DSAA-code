numbers_list = [3, 5, -4, 6, 2]
target = 10

numbers_list.sort()

for x in range(0, len(numbers_list)-2):
    for y in range(x+1, len(numbers_list)-1):
        for z in range(y+1, len(numbers_list)):
            if numbers_list[x] + numbers_list[y] + numbers_list[z] == target:
                print(numbers_list[x], " and ", numbers_list[y], " and ",  + numbers_list[z], " add up to to ", target)
