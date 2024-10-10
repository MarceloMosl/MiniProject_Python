from addTask import addTask
from viewTasks import viewTasks


def switch(value, taskList: list):
    switcher = {
        "1": lambda: addTask(input("Enter the task: "), taskList),
        "2": lambda: print("Option 2"),
        "3": lambda: viewTasks(taskList),
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose one the VALID options :D")
    )()


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
