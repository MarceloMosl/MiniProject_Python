from addTask import addTask
from viewTasks import viewTasks

def removeTask(taskList: list):
    if not taskList:
        print("The task list is empty, nothing to remove.")
    else:
        viewTasks(taskList)
        try:
            taskNumber = int(input("\nEnter the task number to remove: "))
            if 1 <= taskNumber <= len(taskList):
                removedTask = taskList.pop(taskNumber - 1)
                print(f"Task '{removedTask}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def switch(value, taskList: list):
    switcher = {
        "1": lambda: addTask(input("Enter the task: "), taskList),
        "2": lambda: removeTask(taskList),
        "3": lambda: viewTasks(taskList),
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose one the VALID options :D")
    )()


def main():
    programShouldRun = True
    taskList = []


    while programShouldRun:
        print("\n\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        userInput = input("Enter your choice: ")

  

        # check if the user wants to exit
        if userInput == "4":
            programShouldRun = False
            print("Exiting the application. Goodbye!")
            break

        switch(userInput, taskList=taskList)


main()
