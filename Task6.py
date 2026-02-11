import json


try :

    js_in = ipnut('Example: {"name": "Anna", "age": 21}: ')

    data = json.load(js_in)

    age = data['age']
    print(age)

except json.JSONDecodeError:
    print("Error: The string provided is not a valid JSON.")

except KeyError:
    print("Error: The key 'age' was not found in the data.")

