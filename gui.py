import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")

window = gui.Window('Todos to do',
                    layout=[[label], [input_box, add_button],
                            [list_box, edit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()  # read method displays the window on the screen
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break

window.close()
