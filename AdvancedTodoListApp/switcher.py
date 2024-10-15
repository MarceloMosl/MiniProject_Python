from functions.addTask import addTask
from functions.viewTasks import viewTasks
from functions.removeTask import removeTask
from functions.suggestTask import suggestTask


def switch(value, taskList: list):
    switcher = {
        "1": lambda: addTask(taskList),  # add a task
        "2": lambda: removeTask(taskList),  # remove a task
        "3": lambda: viewTasks(taskList),  # view tasks
        "4": lambda: suggestTask(
            suggestTask
        ),  # suggest tasks based on priority and deadlines
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
