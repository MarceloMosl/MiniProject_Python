from addTask import addTask
from viewTasks import viewTasks
from removeTask import removeTask

def switch(value, taskList: list):
    switcher = {
        "1": lambda: addTask(input("Enter the task: "), taskList),
        "2": lambda: removeTask(taskList),
        "3": lambda: viewTasks(taskList),
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose one the VALID options :D")
    )()
