
one_d = list() #[]

one_d.append(1)

one_d.append("Hello")
one_d.append(3.5)
one_d.append('c')
print("One dimensional arrray: ", one_d)

another_one_d = []
another_one_d.append("hi")
another_one_d.append("1")
another_one_d.append(6.58)

two_d = []
two_d.append(one_d)
two_d.append(another_one_d)

print("Two dimensional array: ", two_d)

#creates a 2d array with 1,2,3,4,5,6,7,8,9
another_two_d = []
one = []
two = []
three = []

one.append(1)
one.append(2)
one.append(3)

two.append(4)
two.append(5)
two.append(6)

three.append(7)
three.append(8)
three.append(9)

another_two_d.append(one)
another_two_d.append(two)
another_two_d.append(three)

print("[")
for one_d in another_two_d:
    
    print(one_d)
print("]")

"""
a = [

    [1,2,3]
    [4,5,6]
    [7,8,9]

]

for row in a:
    print(row)
"""