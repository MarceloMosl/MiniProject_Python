from datetime import datetime


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

    for task in sort_tasks:
        print(
            f"{task['description']} - {task['priority'].capitalize()} - {task['deadline']}"
        )
