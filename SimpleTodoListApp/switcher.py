from functions.addTask import addTask
from functions.viewTasks import viewTasks
from functions.removeTask import removeTask


def switch(value, taskList: list):
    switcher = {
        "1": lambda: addTask(taskList),
        "2": lambda: removeTask(taskList),
        "3": lambda: viewTasks(taskList),
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose one the VALID options :D")
    )()
