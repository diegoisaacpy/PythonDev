fname = 'romeo.txt'
fh = open(fname)
lst = list()
newStr = str()
for line in fh:
    newStr += line
for word in newStr.split():
    if word in lst:
        continue
    else:
        lst.append(word)

lst.sort()
print(lst)


#ns = newStr.split()
#print(ns)
#ns.sort()
#print(ns)
