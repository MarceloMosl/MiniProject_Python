def addTask(taskList):
    task = input("Enter the task: ")
    priority = input("Enter the priority (high, medium, low): ").lower()
    deadline = input("Enter the deadline (YYYY-MM-DD): ")

    taskList.append({
        "description": task,
        "priority": priority,
        "deadline": deadline
    })
    print(f"'{task}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")

