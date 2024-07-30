n = int(input("Enter size of triangle: "))

i = 0 
stars = "*"

for k in range(n-1):
    stars = stars + " "

final_print = stars
lastline = stars
k = 0
l = len(stars)-1
while i < n:
    topline = str(lastline)
    
    topline[k] = " "
    topline[l] = " "
    final_print += topline + "\n" + final_print
    lastline = str(topline)

    print(stars)
    index = len(stars)/2
    stars[index] = "*"
    stars = "*" + stars + "*"
    i += 1