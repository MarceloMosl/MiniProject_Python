from addTask import addTask
from viewTasks import viewTasks
from removeTask import removeTask

def switch(value, taskList: list):
    switcher = {
        "1": lambda: addTask(input("Enter the task: "), taskList),
        "2": lambda: removeTask(taskList),
        "3": lambda: viewTasks(taskList),
        "4": lambda: print("Option 4"),  # suggest tasks based on priority and deadlines
    }
    switcher.get(
        value, lambda: print("Invalid option, please choose a valid option.")
    )()


def main():
    programShouldRun = True
    taskList = []

    while programShouldRun:
        # display the menu options
        print("\n\nAdvanced To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Suggest Tasks")
        print("5. Exit")

        # get user input
        userInput = input("Enter your choice: ")

        # check if the user wants to exit
        if userInput == "5":
            programShouldRun = False
            print("Exiting the application. Goodbye!")
            break

        # call the switch function to handle the menu option
        switch(userInput, taskList=taskList)


# run the application
if __name__ == "__main__":
    main()
