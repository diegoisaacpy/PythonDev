file = open("members.txt", "r")
list = file.readlines()
file.close()
member = input("Add a new member: ") + '\n'
list.append(member)
file = open("members.txt", "w")
list = file.writelines(list)
file.close()




