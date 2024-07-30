import random

def generate_array_between(size_array:int, lower: int, upper: int):
    if size_array <= 0:
        return []
    array = [0] * size_array
    for i in range(size_array):
        array[i] = random.randrange(lower, upper)

    return array


