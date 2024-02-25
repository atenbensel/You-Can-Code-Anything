class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks scheduled yet.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.name} - Due Date: {task.due_date}")

def main():
    task_scheduler = TaskScheduler()

    print("Welcome to the Task Scheduler App!")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the task name: ")
            due_date = input("Enter the due date: ")
            task = Task(name, due_date)
            task_scheduler.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            task_scheduler.view_tasks()
        elif choice == '3':
            print("Thank you for using the Task Scheduler App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
