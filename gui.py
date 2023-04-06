#import Modules
import PySimpleGUI as sg

label = sg.Text("Type in Todo list")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

## window accepts the objects row by row
##fjjfj
window = sg.Window('My TO-Do App', layout =[[label], [input_box],[add_button]])

window.read()
window.close() 