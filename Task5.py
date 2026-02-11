import math

try :
    flo = float(input())


    if flo <0:
        raise ValueError('number < 0')


    print(math.sqrt(flo))

except ValueError:
    print('the input is not a number')

