from advanceSwitcher import switch

def main():
    programShouldRun = True
    taskList = []
    completedTasks = []

    while programShouldRun:
        # display the menu options
        print("\n\nAdvanced To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Suggest Tasks")
        print("5. Complete Tasks")
        print("6. Exit")

        # get user input
        userInput = input("Enter your choice: ")

        # check if the user wants to exit
        if userInput == "6":
            programShouldRun = False
            print("Exiting the application. Goodbye!")
            break

        # call the switch function to handle the menu option
        switch(userInput, taskList=taskList, completedTasks=completedTasks)


# run the application
if __name__ == "__main__":
    main()
