from functions import *

(number1, number2) = get_two_numbers_from_user()

#print()
print("Enter e to compute ", number1, " to the power of ", number2)
print("Enter c to compuete the cosine of ", number1)
print("Enter sinn to compute the sine of ", number1)
print("Enter t to compute the tangent of ", number1)
operation = str(input("Enter option: ")).lower()
e = "e"
c = "c"
sinn = "sinn"
t = "t"

x = float(number1)
y = float(number2)
if operation == e:
    result = exponent(x, y)
elif operation == c:
    result = cosine(x)
elif operation == sinn:
    result = sine(x)
elif operation == t:
    result = tangent(x)

print(number1, " ", operation, " ", number2, " = ", result)