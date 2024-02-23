# Define an empty list to store the tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to delete a task from the list
def delete_task():
    print("Current tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    choice = int(input("Enter the number of the task to delete: "))
    if 1 <= choice <= len(tasks):
        del tasks[choice - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid choice.")

