
items = ["apple", "banana", "cherry"]

try :
    idx =  int(input())

    print(items[idx])

except ValueError:
    print('index is not an integer')

except IndexError:
    print('index out of range')

