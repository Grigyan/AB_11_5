prices = {"milk": 2.5, "bread": 1.8, "eggs": 3.2}


try :
    pro = input()

    print(prices[pro])

except KeyError:
    print('we have only milk, bread and eggs')

