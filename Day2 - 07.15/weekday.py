days = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday"] 

day_index = int(input("Enter the day index of the week: "))

for i in range(len(days)):
    if day_index == i: #if i == day_index
        print(days[i])
        break
