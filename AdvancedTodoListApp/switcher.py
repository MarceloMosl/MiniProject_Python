def switch(value, taskList: list):
    switcher = {
        "1": lambda: print("Option 1"),  # add a task
        "2": lambda: print("Option 2"),  # remove a task
        "3": lambda: print("Option 3"),  # view tasks
        "4": lambda: print("Option 4"),  # suggest tasks based on priority and deadlines
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()
