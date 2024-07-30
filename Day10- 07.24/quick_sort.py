from sorting_utilities import generate_array_between

def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)

def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i = i +1
            (a[i], a[j]) = (a[j], a[i])
            
    (a[i+1], a[r]) = (a[r], a[i+1])
    
    return i+1

a1 = generate_array_between(10, 0, 10)
print("before sorted: ", a1)
quick_sort(a1, 0, len(a1)-1)
print(a1)