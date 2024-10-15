def viewTasks(tasksList: list):
    if len(tasksList) == 0:
        print("No tasks to do!!! Have a break, have a Kit Kat.")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasksList, start=1):
        description = task["description"]
        priority = task["priority"]
        deadline = task["deadline"]
        print(f"{i}. {description.capitalize()} - {priority.capitalize()} - {deadline}")
