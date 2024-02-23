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

# Function to display all tasks in the list
def display_tasks():
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Main function to run the to-do list program
def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Thank you for using the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
