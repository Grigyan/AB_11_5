import pdb

def find_max_value(numbers):
    max_value = 0
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value

data = [-5, -2, -10]

print(find_max_value(data))
