import functions
import time

currentTime = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", currentTime)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()  # strip to remove white space while asking for user action

    if user_action.startswith("add"):
        todo = user_action[4:].strip() + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)  # only 1 arg, filepath is default arg

    elif user_action.startswith("show"):
        todos = functions.get_todos()

#  new_todos = [item.strip('\n') for item in todos] list comprehension
        for index, item in enumerate(todos):
            item = item.strip('\n')     # removes new line
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number-1

            """todos_to_edit = todos[number]
            print(todos_to_edit)"""

            todos = functions.get_todos()

            new_todo = input("Enter new todos: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your Command is not valid, Try again")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todos '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid Command")
print("See ya!!")
