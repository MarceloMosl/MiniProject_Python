from switcher import switch


def main():
    programShouldRun = True
    taskList = []

    while programShouldRun:
        print("\n\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        userInput = input("Enter your choice: ")

        # check if the user wants to exit
        if userInput == "4":
            programShouldRun = False
            print("Exiting the application. Goodbye!")
            break

        switch(userInput, taskList=taskList)


main()
