import sys
import json
from Functions import *
from Task import *

tasks = []

try:
    with open("tasks.json", "r") as file:
        data = json.load(file)
        for item in data:
            tasks.append(Task.from_dict(item))
except FileNotFoundError as e:
    pass

show_menu()

while True:
    user_input = input("\nEnter an input: ")
    if user_input == "show":
        show_tasks(tasks)

    elif user_input == "exit":
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent = 4)
        sys.exit()

    elif user_input == "delete":
        delete_task(tasks)

    elif user_input == "complete":
        complete_task(tasks)

    elif user_input == "help":
        show_menu()

    elif user_input =="edit":
        edit_task(tasks)

    else:
        new_task = Task(user_input)
        tasks.append(new_task)






