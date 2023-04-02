#Count the characters contained in the file
file = open("essay.txt", "r")
content = file.read()
print(len(content))