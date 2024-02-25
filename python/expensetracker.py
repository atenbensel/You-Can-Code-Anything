class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("Expenses:")
            for expense in self.expenses:
                print(f"Amount: {expense['amount']}, Category: {expense['category']}")

    def analyze_expenses(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: {total_expenses}")

def main():
    expense_tracker = ExpenseTracker()

    print("Welcome to the Expense Tracker App!")

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            expense_tracker.add_expense(amount, category)
            print("Expense added successfully.")
        elif choice == '2':
            expense_tracker.view_expenses()
        elif choice == '3':
            expense_tracker.analyze_expenses()
        elif choice == '4':
            print("Thank you for using the Expense Tracker App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
