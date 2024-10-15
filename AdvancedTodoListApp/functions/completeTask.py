def completeTasks(tasksList: list, completedTasks: list):
    print("What task would you like to mark as done?")

    search = input("Search by name: ")

    # Display the matching tasks
    matching_tasks = []
    for i in range(len(tasksList)):
        crrntTask = tasksList[i]
        if search.lower() in crrntTask["description"].lower():
            matching_tasks.append((i, crrntTask))
            print(
                f"{i+1} - {crrntTask['description']} - {crrntTask['priority']} - {crrntTask['deadline']}"
            )

    if not matching_tasks:
        print("No tasks found with that name.")
        return

    while True:
        taskToComplete = input(
            "\nPress Q to search one more time.\nPlease select the number of the task you would like to complete: "
        )

        # Allow the user to search again
        if taskToComplete.lower() == "q":
            completeTasks(tasksList, completedTasks)
            break

        # Validate that the input is a number and in the valid range
        if taskToComplete.isdigit():
            taskToComplete = int(taskToComplete) - 1
            if 0 <= taskToComplete < len(tasksList):
                # Task is valid
                completedTasks.append(tasksList[taskToComplete])
                tasksList.pop(taskToComplete)
                print("Task completed, one less to do!!!")
                break
            else:
                print("Invalid number! Please select a number from the list.")
        else:
            print("Invalid input! Please enter a valid number or 'Q' to search again.")
