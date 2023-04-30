while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            with open('./TodoListApp/todos.txt', 'r') as file:
                todos = file.readlines()
                file.close()

            # Crea una lista con el contenido de las lineas
            todos.append(todo)
            # Añade la nueva linea y lo une a la lista todos.

            with open('./TodoListApp/todos.txt', 'w') as file:
                todos = file.writelines(todos)
            # Escribe nuevas lineas en el txt
        case 'show':

            with open('./TodoListApp/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
