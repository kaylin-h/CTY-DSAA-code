def fact(n):

    print("Completing factorial of ", n)
    if n < 0:
        print("Can't do it")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
def while_fact(n):
    product = 1

    if n < 0:
        n = n * (-1)
    for i in range(2, n+1):
        product *= i

    return product 

    

print("Factorial of 5 is ", while_fact(-5))