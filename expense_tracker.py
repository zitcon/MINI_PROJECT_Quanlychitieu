import os
import json

DATA_FILE = "expenses.txt"
JSON_FILE = "expenses.json"


def load_expenses(filename):
    expenses = []
    if not os.path.exists(filename):
        return expenses

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("|")
            if len(parts) != 5:
                continue

            expense = {
                "id": parts[0],
                "date": parts[1],
                "category": parts[2],
                "description": parts[3],
                "amount": float(parts[4])
            }
            expenses.append(expense)

    return expenses


def save_expenses(filename, expenses):
    with open(filename, "w", encoding="utf-8") as file:
        for expense in expenses:
            line = (
                f"{expense['id']}|"
                f"{expense['date']}|"
                f"{expense['category']}|"
                f"{expense['description']}|"
                f"{expense['amount']}\n"
            )
            file.write(line)


def is_duplicate_id(expenses, expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return True
    return False


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Input cannot be empty. Please try again.")


def input_positive_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number > 0:
                return number
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses):
    print("\n=== ADD NEW EXPENSE ===")

    while True:
        expense_id = input_non_empty("Enter expense ID: ")
        if is_duplicate_id(expenses, expense_id):
            print("This ID already exists. Please enter another ID.")
        else:
            break

    date = input_non_empty("Enter date (YYYY-MM-DD): ")
    category = input_non_empty("Enter category: ")
    description = input_non_empty("Enter description: ")
    amount = input_positive_float("Enter amount: ")

    new_expense = {
        "id": expense_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(new_expense)
    save_expenses(DATA_FILE, expenses)
    print("Expense added successfully and saved to file.")


def display_expenses(expenses):
    print("\n=== EXPENSE LIST ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print(f"{'ID':<10}{'DATE':<15}{'CATEGORY':<20}{'DESCRIPTION':<30}{'AMOUNT':>12}")
    print("-" * 87)

    for expense in expenses:
        print(
            f"{expense['id']:<10}"
            f"{expense['date']:<15}"
            f"{expense['category']:<20}"
            f"{expense['description']:<30}"
            f"{expense['amount']:>12.2f}"
        )


def search_by_exact_id(expenses):
    print("\n=== SEARCH BY EXACT ID ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    target_id = input("Enter exact expense ID to search: ").strip()
    found = False

    for expense in expenses:
        if expense["id"] == target_id:
            print("\nFound expense:")
            print(f"ID: {expense['id']}")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Amount: {expense['amount']:.2f}")
            found = True
            break

    if not found:
        print("No expense found with that ID.")


def sort_by_amount_ascending(expenses):
    print("\n=== SORT BY AMOUNT (ASCENDING) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["amount"])
    display_expenses(sorted_expenses)


def show_basic_statistics(expenses):
    print("\n=== BASIC STATISTICS ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0
    for expense in expenses:
        total += expense["amount"]

    average = total / len(expenses)

    print(f"Total number of expenses: {len(expenses)}")
    print(f"Total spending: {total:.2f}")
    print(f"Average expense: {average:.2f}")


def display_menu():
    print("\n========== PERSONAL FINANCE / EXPENSE TRACKER ==========")
    print("1. Add new expense")
    print("2. Display all expenses")
    print("3. Search expense by exact ID")
    print("4. Sort expenses by amount (ascending)")
    print("5. Show basic statistics")
    print("0. Exit")


def main():
    expenses = load_expenses(DATA_FILE)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            search_by_exact_id(expenses)
        elif choice == "4":
            sort_by_amount_ascending(expenses)
        elif choice == "5":
            show_basic_statistics(expenses)
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter again.")


if __name__ == "__main__":
    main()