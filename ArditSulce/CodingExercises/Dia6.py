new_member = input("Give me the name of the new member:") + "\n"
file = open("members.txt", "r")
content = file.readlines()
file.close()

content.append(new_member + "\n")

file = open("members.txt", "w")
file.writelines(content)
file.close()