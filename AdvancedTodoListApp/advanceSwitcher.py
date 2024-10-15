from functions.addTask import addTask
from functions.viewTasks import viewTasks
from functions.removeTask import removeTask
from functions.suggestTask import suggestTask
from functions.completeTask import completeTasks
from functions.completesChart import completesChart


def switch(value, taskList: list, completedTasks: list):
    switcher = {
        "1": lambda: addTask(taskList),  # add a task
        "2": lambda: removeTask(taskList),  # remove a task
        "3": lambda: viewTasks(taskList),  # view tasks
        "4": lambda: suggestTask(
            taskList
        ),  # suggest tasks based on priority and deadlines
        "5": lambda: completeTasks(tasksList=taskList, completedTasks=completedTasks),
        "6": lambda: completesChart(tasks=completedTasks),
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
