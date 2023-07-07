from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, complete, show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:] + '\n'
        todos = get_todos("todos.txt")
        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1} - {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except:
            print("There is no item with that description")
            continue



    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
        break

print("Bye")
