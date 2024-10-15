from addTask import addTask
from suggestTask import suggestTask
from viewTasks import viewTasks
from removeTask import removeTask

def switch(userInput, taskList):
    if userInput == "1":
        addTask(taskList)
    elif userInput == "2":
        removeTask(taskList)
    elif userInput == "3":
        viewTasks(taskList)
    elif userInput == "4":
        suggestTask(taskList)


    else:
        print("Invalid choice, please try again.")