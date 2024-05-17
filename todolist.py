import json
import os

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    return tasks

def update_task(tasks, index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]['task'] = new_task
    return tasks

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
    return tasks

def list_tasks(tasks):
    for index, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. List Tasks")
    print("6. Exit")

def main():
    filename = 'todo.json'
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks = add_task(tasks, task)
            save_tasks(tasks, filename)
        elif choice == '2':
            list_tasks(tasks)
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            tasks = update_task(tasks, index, new_task)
            save_tasks(tasks, filename)
        elif choice == '3':
            list_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            tasks = delete_task(tasks, index)
            save_tasks(tasks, filename)
        elif choice == '4':
            list_tasks(tasks)
            index = int(input("Enter task number to complete: ")) - 1
            tasks = complete_task(tasks, index)
            save_tasks(tasks, filename)
        elif choice == '5':
            list_tasks(tasks)
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
