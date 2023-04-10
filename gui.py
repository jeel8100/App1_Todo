import functions
import PySimpleGUI as sg

label = sg.Text("Type in Todo list")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")


# window accepts the objects row by row

window = sg.Window('My TO-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button ]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    """Values -> Dictionary """
    match event:
        case "Add":
            todos = functions.get_todos()
            """Storing the new input in new variable through key[todo]"""
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            """Add the updated todo list to todo.txt"""
            functions.write_todos(todos)
            # update the list box with the latest values
            window['todos'].update(values=todos)
        case 'todos':
            # when clicking on list box, it should update data or list
            window['todo'].update(value=values['todos'][0])

        case "Edit":
            # getting the selected item from list
            todo_to_edit = values['todos'][0]
            # getting the new value to update the item (input box)
            new_todo = values['todo']

            todos = functions.get_todos()
            # index of org item from list
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            # update the list box
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break


window.close()
