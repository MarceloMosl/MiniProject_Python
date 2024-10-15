from datetime import datetime


def get_valid_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            parsed_date = datetime.strptime(date_input, "%Y-%m-%d")

            # Check if the date is today or later
            if parsed_date >= datetime.today():
                return date_input
            else:
                print(
                    "The date must be today or later. Unless you have a time machine, please enter a valid date."
                )
        except ValueError:
            print(
                f"Invalid date format. Please enter the date in the format YYYY-MM-DD."
            )


def addTask(taskList: list):
    task = input("Enter the task: ")

    priority = input("Enter the priority (high, medium or low): ").lower()
    priority_mapping = {"high", "medium", "low"}

    # Check if the user input is a valid option for the task priority
    while priority not in priority_mapping:
        print("Invalid option, please choose a valid option.")
        priority = input("Enter the priority (high, medium or low): ").lower()

    deadline = get_valid_date("Enter the deadline (YYYY-MM-DD): ")

    # Check for duplicate tasks
    for t in taskList:
        if t["description"] == task and t["deadline"] == deadline:
            print(
                "\nThis task has already been added to the list, try adding another one! :D"
            )
            return

    taskList.append({"description": task, "priority": priority, "deadline": deadline})
    print(
        f"'{task}' with priority '{priority.capitalize()}' and deadline '{deadline}' has been added to the list."
    )
