files = ['a.txt', 'b.txt', 'c.txt']

for filename in files:
    x = open(filename, "r")
    print(x.read())
