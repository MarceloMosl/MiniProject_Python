from functions.viewTasks import viewTasks


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
                print(
                    "Invalid task number. Please choose a valid number from the list."
                )
        except ValueError:
            print("Please enter a valid number.")
