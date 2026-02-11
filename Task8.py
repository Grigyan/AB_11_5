
class  InvalidAgeError(Exception):
    pass

def check_age(age):

    try :
        age = int(age)
        if (age <18) or (age > 200):
            raise InvalidAgeError('valid age range: 18..120')
        print( "Age accepted.")

    except ValueError:
        print('non-integer input')





inp = input()

check_age(inp)