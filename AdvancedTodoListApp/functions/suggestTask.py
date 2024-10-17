from datetime import datetime # Allows access to date and time functions

time = datetime.now().hour # Getting the current hour from the system's date and time

def suggestTask(taskList): # Defines a function that takes one argument, taskList.
    if not taskList: # Checking if the task list is empty
        print("The task list is empty, nothing to suggest.")
        return

    priority_order = {"high": 1, "medium": 2, "low": 3} #Define the priority order for sorting the tasks
    sort_tasks = sorted( # Sorting task
        taskList,
        key=lambda x: (
            datetime.strptime(
                x["deadline"], "%Y-%m-%d"
            ),  # Sort by deadline (earliest first)
            priority_order[x["priority"]],  # Sort by priority (high > medium > low)
        ),
    )

#This block checks the current hour and prints an appropriate greeting.
    if 5 <= time < 12:
        print("\nGood morning! Here are some tasks you might want to work on:")
    elif 12 <= time < 18:
        print("\nGood afternoon! Here are some tasks you might want to work on:")
    elif 18 <= time < 21:
        print("\nGood evening! Here are some tasks you might want to work on:")
    else:
        print("\nGood night! Here are some tasks you might want to work on:")

    for task in sort_tasks: # this loop iterates over the sorted tasks and prints each task's description
        print(f"{task['description']} - {task['priority'].capitalize()} - {task['deadline']}")
