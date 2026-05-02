def show_menu():
    print("Available commands:")
    print("- show")
    print("- delete")
    print("- complete")
    print("- exit")
    print("- edit")
    print("- help")
    print("Or just type a new task to add it.")

def show_tasks(task_list):
    index = 1
    for task in task_list:
        if task.is_completed:
            print("[X] " + str(index) + ") " + task.explanation)
        else:
            print("[ ] " + str(index) + ") " + task.explanation)
        index += 1

def delete_task(task_list):
    delete_index = int(input("Which task do you want to delete?: "))
    if delete_index < 1 or delete_index > len(task_list):
        print("Please enter a valid number.")
    else:
        print("Task successfully deleted.")
        task_list.pop(delete_index - 1)


def complete_task(task_list):
    complete_index = int(input("Which task do you want to complete?: "))
    if complete_index < 1 or complete_index > len(task_list):
        print("Please enter a valid number.")
    else:
        task_list[complete_index - 1].is_completed = True

def edit_task(task_list):
    edit_index = int(input("Which task do you want to edit?: "))
    if edit_index < 1 or edit_index > len(task_list):
        print("Please enter a valid number.")
    else:
        new_explanation = input("Enter new task: ")
        task_list[edit_index - 1].explanation = new_explanation


