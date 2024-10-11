def addTask(taskList: list):
    newTask = input("Enter the task: ")
    if newTask not in taskList:
        taskList.append(newTask)
        print(f"'{newTask}' has been added to the list")
    else:
        print(f"'{newTask}' has already been added to the list, try a different one")
