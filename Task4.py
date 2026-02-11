try :
    filename = input('filename: ')

    with open(filename, 'r') as f:
        print(f.read())

except FileNotFoundError:
    print('Not found that file ')

except PermissionError:
    print('PermissionError')

finally:
    print("Finished file attempt.")

