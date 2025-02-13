#Main code behind a CLI Task Manager

import json  # For saving and loading tasks
import argparse  # For command-line arguments
import uuid  # For generating unique task IDs
from datetime import datetime  # For handling due dates
from colorama import Fore, Style  # For colored text

class Task():
    def __innit__(self, title, due_date=None, priority=3):
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

