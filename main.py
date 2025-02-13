#Main code behind a CLI Task Manager

import json  # For saving and loading tasks
import argparse  # For command-line arguments
import uuid  # For generating unique task IDs
from datetime import datetime  # For handling due dates
from colorama import Fore, Style  # For colored text

class Task:
    def __init__(self, title, due_date=None, priority=3):
        self.id = str(uuid.uuid4())
        self.title = title
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.due_date = due_date
        self.priority = priority

    def to_dict(self):
        return self.__dict__

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, due_date, priority):
    tasks = load_tasks()
    new_task = Task(title, due_date, priority)
    tasks.append(new_task.to_dict())
    save_tasks(tasks)
    print(f"{Fore.GREEN}Task added: {new_task.title}{Style.RESET_ALL}")

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"{Fore.CYAN}{task['title']} (Due: {task['due_date']}){Style.RESET_ALL}")

def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"{Fore.RED}Task deleted{Style.RESET_ALL}")
            return
    print(f"{Fore.RED}Task not found{Style.RESET_ALL}")

parser = argparse.ArgumentParser(description="CLI Task Manager")
parser.add_argument("command", choices=["add", "list", "delete"], help="Action to perform")
parser.add_argument("--title", help="Title of the task")
parser.add_argument("--due_date", help="Due date of the task (YYYY-MM-DD)")
parser.add_argument("--priority", type=int, choices=range(1, 4), default=3, help="Priority of the task (1-3, 3 being highest)")

args = parser.parse_args()

if args.command == "add":
    add_task(args.title, args.due_date, args.priority)
elif args.command == "list":
    list_tasks()
elif args.command == "delete":
    delete_task(args.title)
else:
    print(f"{Fore.RED}Invalid command{Style.RESET_ALL}")