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

            try:
                expense = {
                    "id": parts[0],
                    "date": parts[1],
                    "category": parts[2],
                    "description": parts[3],
                    "amount": float(parts[4])
                }
                expenses.append(expense)
            except ValueError:
                continue

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


def export_to_json(filename, expenses):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def is_duplicate_id(expenses, expense_id):
    for expense in expenses:
        if expense["id"].lower() == expense_id.lower():
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


def print_table_header():
    print(f"{'ID':<10}{'DATE':<15}{'CATEGORY':<20}{'DESCRIPTION':<30}{'AMOUNT':>12}")
    print("-" * 87)


def print_expense_row(expense):
    print(
        f"{expense['id']:<10}"
        f"{expense['date']:<15}"
        f"{expense['category']:<20}"
        f"{expense['description']:<30}"
        f"{expense['amount']:>12.2f}"
    )


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

    print_table_header()
    for expense in expenses:
        print_expense_row(expense)


def search_by_exact_id(expenses):
    print("\n=== SEARCH BY EXACT ID ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    target_id = input("Enter exact expense ID to search: ").strip()
    found = False

    for expense in expenses:
        if expense["id"].lower() == target_id.lower():
            print("\nFound expense:")
            print_table_header()
            print_expense_row(expense)
            found = True
            break

    if not found:
        print("No expense found with that ID.")


def search_by_keyword(expenses):
    print("\n=== ADVANCED SEARCH BY KEYWORD ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    keyword = input("Enter keyword (category/description/date): ").strip().lower()
    if keyword == "":
        print("Keyword cannot be empty.")
        return

    results = []
    for expense in expenses:
        if (
            keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
            or keyword in expense["date"].lower()
            or keyword in expense["id"].lower()
        ):
            results.append(expense)

    if len(results) == 0:
        print("No matching expenses found.")
        return

    print(f"\nFound {len(results)} matching expense(s):")
    print_table_header()
    for expense in results:
        print_expense_row(expense)


def sort_by_amount_ascending(expenses):
    print("\n=== SORT BY AMOUNT (ASCENDING) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["amount"])
    print_table_header()
    for expense in sorted_expenses:
        print_expense_row(expense)


def sort_by_amount_descending(expenses):
    print("\n=== SORT BY AMOUNT (DESCENDING) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["amount"], reverse=True)
    print_table_header()
    for expense in sorted_expenses:
        print_expense_row(expense)


def sort_by_category_a_to_z(expenses):
    print("\n=== SORT BY CATEGORY (A-Z) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["category"].lower())
    print_table_header()
    for expense in sorted_expenses:
        print_expense_row(expense)


def show_basic_statistics(expenses):
    print("\n=== BASIC STATISTICS ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0
    for expense in expenses:
        total += expense["amount"]

    average = total / len(expenses)
    highest = max(expenses, key=lambda item: item["amount"])
    lowest = min(expenses, key=lambda item: item["amount"])

    print(f"Total number of expenses: {len(expenses)}")
    print(f"Total spending: {total:.2f}")
    print(f"Average expense: {average:.2f}")
    print(f"Highest expense: {highest['description']} - {highest['amount']:.2f}")
    print(f"Lowest expense: {lowest['description']} - {lowest['amount']:.2f}")


def show_statistics_by_category(expenses):
    print("\n=== ADVANCED STATISTICS BY CATEGORY ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    category_totals = {}
    category_counts = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0
            category_counts[category] = 0

        category_totals[category] += expense["amount"]
        category_counts[category] += 1

    print(f"{'CATEGORY':<20}{'COUNT':<10}{'TOTAL':>12}")
    print("-" * 42)

    for category in sorted(category_totals.keys()):
        print(f"{category:<20}{category_counts[category]:<10}{category_totals[category]:>12.2f}")


def display_sort_menu():
    print("\n=== SORT MENU ===")
    print("1. Sort by amount ascending")
    print("2. Sort by amount descending")
    print("3. Sort by category A-Z")
    print("0. Back to main menu")


def sort_expenses(expenses):
    while True:
        display_sort_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sort_by_amount_ascending(expenses)
        elif choice == "2":
            sort_by_amount_descending(expenses)
        elif choice == "3":
            sort_by_category_a_to_z(expenses)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter again.")


def display_statistics_menu():
    print("\n=== STATISTICS MENU ===")
    print("1. Show basic statistics")
    print("2. Show statistics by category")
    print("0. Back to main menu")


def statistics_menu(expenses):
    while True:
        display_statistics_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_basic_statistics(expenses)
        elif choice == "2":
            show_statistics_by_category(expenses)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter again.")


def display_search_menu():
    print("\n=== SEARCH MENU ===")
    print("1. Search by exact ID")
    print("2. Search by keyword")
    print("0. Back to main menu")


def search_menu(expenses):
    while True:
        display_search_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_by_exact_id(expenses)
        elif choice == "2":
            search_by_keyword(expenses)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter again.")


def display_menu():
    print("\n========== PERSONAL FINANCE / EXPENSE TRACKER ==========")
    print("1. Add new expense")
    print("2. Display all expenses")
    print("3. Search")
    print("4. Sort")
    print("5. Statistics")
    print("6. Export to JSON")
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
            search_menu(expenses)
        elif choice == "4":
            sort_expenses(expenses)
        elif choice == "5":
            statistics_menu(expenses)
        elif choice == "6":
            export_to_json(JSON_FILE, expenses)
            print(f"Data exported successfully to {JSON_FILE}.")
        elif choice == "0":
            save_expenses(DATA_FILE, expenses)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter again.")


if __name__ == "__main__":
    main()