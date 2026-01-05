import argparse
import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    new_task = {
        'task': description,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: '{description}'")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\n--- To-Do List ---")
    for index, task in enumerate(tasks, 1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['task']}")
    print("------------------\n")

def complete_task(index):
    tasks = load_tasks()
    adjusted_index = index - 1
    
    if 0 <= adjusted_index < len(tasks):
        tasks[adjusted_index]['completed'] = True
        save_tasks(tasks)
        print(f"Task {index} marked as done.")
    else:
        print(f"Error: Task number {index} does not exist.")

def delete_task(index):
    tasks = load_tasks()
    adjusted_index = index - 1
    
    if 0 <= adjusted_index < len(tasks):
        removed = tasks.pop(adjusted_index)
        save_tasks(tasks)
        print(f"Task '{removed['task']}' deleted.")
    else:
        print(f"Error: Task number {index} does not exist.")

def main():
    parser = argparse.ArgumentParser(description="A Simple CLI To-Do List")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="The task description")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("index", type=int, help="Task number to complete")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task number to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()