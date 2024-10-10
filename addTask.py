def addTask(newTask: str, taskList: list):
  if newTask not in taskList:
      taskList.append(newTask)
      print(f"'{newTask}' has been added to the list")
  else:
    print(f"'{newTask}' has already been added to the list, try a different one")
