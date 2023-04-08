FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write items in to-do list """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "--main":
    print("Hello")
    print(get_todos())
