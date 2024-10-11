def viewTasks(tasksList: list):

    if len(tasksList) == 0:
        print("No tasks to do!!! Have a break have a Kit Kat")
        return

    print("\nTo-Do List:")
    for i in range(len(tasksList)):
        print(f"{i+1}. {tasksList[i].capitalize()}")
