import PySimpleGUI as gui
import time
import functions

# Use a more modern theme
gui.theme('DarkAmber')

# Define enhanced layout with icons, button colors, and better organization
label_clock = gui.Text('', key="clock", justification='center', font=('Helvetica', 14))
label = gui.Text("What needs to be done?", font=('Helvetica', 16), pad=(10, 10))

input_box = gui.InputText(tooltip="Enter your task", key="todo", size=(30, 1), font=('Helvetica', 14))
add_button = gui.Button("➕ Add", size=(10, 1), button_color=("white", "#27ae60"), font=('Helvetica', 14),
                        tooltip="Add task")
list_box = gui.Listbox(values=functions.get_todos(), key="todos", select_mode=gui.LISTBOX_SELECT_MODE_SINGLE,
                       enable_events=True, size=(40, 10), font=('Helvetica', 14))

edit_button = gui.Button("✏️ Edit", size=(10, 1), button_color=("white", "#3498db"), font=('Helvetica', 14),
                         tooltip="Edit selected task")
complete_button = gui.Button("✔️ Complete", size=(10, 1), button_color=("white", "#e74c3c"), font=('Helvetica', 14),
                             tooltip="Mark as completed")
exit_button = gui.Button("❌ Exit", size=(10, 1), button_color=("white", "#95a5a6"), font=('Helvetica', 14))

window = gui.Window(
    'To-Do List Manager',
    layout=[[label_clock],
            [label],
            [input_box, add_button],
            [list_box],
            [edit_button, complete_button],
            [exit_button]],
    font=('Helvetica', 14),
    element_justification='center',
    finalize=True,
    size=(500, 400)
)

# Start with focus on input box for better UX
window['todo'].set_focus()

while True:
    event, values = window.read(timeout=200)

    # Update clock dynamically
    window['clock'].update(time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "➕ Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip()
            if new_todo:  # Add only if the input is not empty
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')  # Clear input box after adding
                gui.popup("Task added successfully!", font=('Helvetica', 14))
            else:
                gui.popup_error("Please enter a valid task!", font=('Helvetica', 14))

        case "✏️ Edit":
            try:
                selected_todo = values['todos'][0]
                new_todo = values['todo'].strip()
                if new_todo:  # Check if input is non-empty
                    todos = functions.get_todos()
                    index = todos.index(selected_todo)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update('')  # Clear input after editing
                    gui.popup("Task updated successfully!", font=('Helvetica', 14))
                else:
                    gui.popup_error("Please enter a valid task to update!", font=('Helvetica', 14))
            except IndexError:
                gui.popup_error("Please select a task to edit!", font=('Helvetica', 14))

        case "✔️ Complete":
            try:
                selected_todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(selected_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')  # Clear input after completing
                gui.popup("Task completed successfully!", font=('Helvetica', 14))
            except IndexError:
                gui.popup_error("Please select a task to complete!", font=('Helvetica', 14))

        case "❌ Exit":
            if gui.popup_yes_no("Are you sure you want to exit?", font=('Helvetica', 14)) == "Yes":
                break

        case "todos":
            if values['todos']:
                window['todo'].update(value=values['todos'][0])

        case gui.WIN_CLOSED:
            break

window.close()
