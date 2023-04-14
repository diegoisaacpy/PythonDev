file = open("data.txt")
lst = list()
secondList = list()
thirdList = list()
newStr = str()
secondStr = str()
fourthList = list()
for line in file:
    newStr += line
oracionesRenglon = newStr.split("\n")
for element in oracionesRenglon:
    if "From" in element:
        secondList.append(element)
    else:
        continue
for element in secondList:
    secondStr += element

for mail in secondStr.split():
    if "@" in mail:
        if "From" in mail:
            continue
        else:
            fourthList.append(mail)
    else:
        continue
lastList = fourthList[0:-1]
for i in lastList:
    print(i)
print(f"There were {int(len(secondList)/2)} lines in the file with From as first word")
