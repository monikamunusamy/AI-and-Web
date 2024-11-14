# Task Manager Program

def show_tasks(tasks):
    """Display the current tasks."""
    print("\nCurrent Tasks:")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"'{task}' has been added.")

def remove_task(tasks):
    """Remove a task by number."""
    show_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"'{removed_task}' has been removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTask Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
