while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # Crea una lista con el contenido de las lineas
            todos.append(todo)
            # Añade la nueva linea y lo une a la lista todos.

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            # Escribe nuevas lineas en el txt
        case 'show':
            file = open('todos.txt', 'r')  # abrimos
            todos = file.readlines()  # leemos las lineas y obtenemos un list

            file.close()

            for item in todos:
                item = item.strip('\n')
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, item in enumerate(todos):
                row = f"{index + 1} - {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
