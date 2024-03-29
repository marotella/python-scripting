task_list = []

def tasks (task_list):
    task = input("Add a task to the list or press enter to finish: ")
    if len(task) == 0:
        print(task_list)
    else:
        task_list.append(task)
        tasks(task_list)

tasks(task_list)