def addTask(taskList):
    task = input("Enter the task: ")
    priority_mapping = {
        "1": "high",
        "2": "medium",
        "3": "low"
    }
    priority = input("Enter the priority (1. high, 2. medium, 3. low): ").lower()
    priority = priority_mapping.get(priority, "low")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")

    taskList.append({
        "description": task,
        "priority": priority,
        "deadline": deadline
    })
    print(f"'{task}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")

