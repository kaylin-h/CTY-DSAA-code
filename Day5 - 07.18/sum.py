def smart_sum(n):

    if n == 0:
        return 0
    elif n > 0 :
        return n + smart_sum(n-1)
    else:
        return n + smart_sum(n+1)
    
"""
def sigma(n):
    if n < 0:
        return sigma(n * (-1))
    elif n == 0:
        return 0
    else:
        return n + sigma(n-1)

"""
        

print("The sum from 0 to -3 is", smart_sum(-3))
