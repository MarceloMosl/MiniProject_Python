from datetime import datetime

time = datetime.now().hour

def suggestTask(taskList):
    if not taskList:
        print("The task list is empty, nothing to suggest.")
        return

    priority_order = {"high": 1, "medium": 2, "low": 3}
    sort_tasks = sorted(
        taskList,
        key=lambda x: (
            datetime.strptime(
                x["deadline"], "%Y-%m-%d"
            ),  # Sort by deadline (earliest first)
            priority_order[x["priority"]],  # Sort by priority (high > medium > low)
        ),
    )

    if 5 <= time < 12:
        print("\nGood morning! Here are some tasks you might want to work on:")
    elif 12 <= time < 18:
        print("\nGood afternoon! Here are some tasks you might want to work on:")
    elif 18 <= time < 21:
        print("\nGood evening! Here are some tasks you might want to work on:")
    else:
        print("\nGood night! Here are some tasks you might want to work on:")

    for task in sort_tasks:
        print(f"{task['description']} - {task['priority'].capitalize()} - {task['deadline']}")
