import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")

window = gui.Window('Todos to do', layout=[[label], [input_box, add_button]])
window.read()  # read method displays the window on the screen
window.close()

