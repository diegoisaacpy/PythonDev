for filename in 'abc':
    file = open(f'{filename}.txt', "r")
    print(file.read())