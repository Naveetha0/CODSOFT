todo_list = []

# Function to add a new task
def add_task():
    task = input("Enter the Task: ")
    todo_list.append({"task": task, "status": "Pending"})
    print("New Task Added Successfully!\n")

# Function to view all tasks
def view_task():
    print("\nYour Todo List:")
    if len(todo_list) == 0:
        print(" No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['task']} - {task['status']}")
    print()

# Function to remove a task
def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!\n")
    else:
        view_task()  # Show current tasks first
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['task']}\n")
            else:
                print("Invalid Task Number\n")
        except ValueError:
            print("Please enter a valid number!\n")

# Function to mark a task as completed
def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!\n")
    else:
        view_task()  # Show current tasks first
        try:
            task_num = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_num < len(todo_list):
                todo_list[task_num]['status'] = "Completed"
                print("Task marked as completed!\n")
            else:
                print("Invalid Task Number\n")
        except ValueError:
            print("Please enter a valid number!\n")

# Function to display the menu
def menu():
    while True:
        print("*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! Try again!\n")

# Start the program
menu()
