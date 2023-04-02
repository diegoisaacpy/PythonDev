file = open("essay.txt", 'r')
sentence = file.readline()


for i in sentence.rsplit(" "):
    print(i.capitalize())


#Otra solucion

#file = open("essay.txt", 'r')
#sentence = file.read()
#print(sentence.title())