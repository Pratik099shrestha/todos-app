import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window('Todos to do',
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()  # read method displays the window on the screen
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    print(4, values["todo"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break

window.close()
