

try :
    x = int(input())
    print(100/x)

except ValueError:
    print('x id not int')

except ZeroDivisionError:
    print('x is 0')


