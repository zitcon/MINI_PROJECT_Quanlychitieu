import os
import json
from datetime import datetime
from prettytable import PrettyTable

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


def find_expense_index_by_id(expenses, expense_id):
    for index, expense in enumerate(expenses):
        if expense["id"].lower() == expense_id.lower():
            return index
    return -1


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Input cannot be empty. Please try again.")


def input_valid_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            input_date = datetime.strptime(value, "%Y-%m-%d")
            today = datetime.today()

            if input_date > today:
                print("Date cannot be in the future.")
                continue

            return value
        except ValueError:
            print("Invalid date. Please enter date in YYYY-MM-DD format.")


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


def input_category(prompt):
    while True:
        category = input_non_empty(prompt)
        if category.isdigit():
            print("Category must contain text, not just numbers.")
        else:
            return category


def input_description(prompt):
    while True:
        description = input_non_empty(prompt)
        if description.isdigit():
            print("Description must contain text, not just numbers.")
        else:
            return description


def print_expenses_table(expenses, title):
    print(f"\n=== {title} ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Date", "Category", "Description", "Amount"]
    table.align["ID"] = "l"
    table.align["Date"] = "l"
    table.align["Category"] = "l"
    table.align["Description"] = "l"
    table.align["Amount"] = "r"

    for expense in expenses:
        table.add_row([
            expense["id"],
            expense["date"],
            expense["category"],
            expense["description"],
            f"{expense['amount']:.2f}"
        ])

    print(table)


def add_expense(expenses):
    print("\n=== ADD NEW EXPENSE ===")

    while True:
        expense_id = input_non_empty("Enter expense ID (E01, E02...): ")

        if not expense_id.startswith("E"):
            print("ID must start with 'E' (e.g., E01).")
            continue

        if is_duplicate_id(expenses, expense_id):
            print("This ID already exists. Please enter another ID.")
            continue

        break

    date = input_valid_date("Enter date (YYYY-MM-DD): ")
    category = input_category("Enter category: ")
    description = input_description("Enter description: ")
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
    print_expenses_table(expenses, "EXPENSE LIST")


def search_by_exact_id(expenses):
    print("\n=== SEARCH BY EXACT ID ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    target_id = input("Enter exact expense ID to search: ").strip()
    results = []

    for expense in expenses:
        if expense["id"].lower() == target_id.lower():
            results.append(expense)
            break

    if len(results) == 0:
        print("No expense found with that ID.")
        return

    print_expenses_table(results, "SEARCH RESULT")


def search_by_keyword(expenses):
    print("\n=== SEARCH BY KEYWORD ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    keyword = input("Enter keyword: ").strip().lower()
    if keyword == "":
        print("Keyword cannot be empty.")
        return

    results = []
    for expense in expenses:
        if (
            keyword in expense["id"].lower()
            or keyword in expense["date"].lower()
            or keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
            or keyword in str(expense["amount"])
        ):
            results.append(expense)

    if len(results) == 0:
        print("No matching expenses found.")
        return

    print_expenses_table(results, f"FOUND {len(results)} MATCHING EXPENSE(S)")


def search_by_amount_range(expenses):
    print("\n=== SEARCH BY AMOUNT RANGE ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    min_amount = input_positive_float("Enter minimum amount: ")
    max_amount = input_positive_float("Enter maximum amount: ")

    if min_amount > max_amount:
        print("Minimum amount cannot be greater than maximum amount.")
        return

    results = []
    for expense in expenses:
        if min_amount <= expense["amount"] <= max_amount:
            results.append(expense)

    if len(results) == 0:
        print("No matching expenses found.")
        return

    print_expenses_table(results, f"EXPENSES FROM {min_amount:.2f} TO {max_amount:.2f}")


def search_by_date_range(expenses):
    print("\n=== SEARCH BY DATE RANGE ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    start_date = input_valid_date("Enter start date (YYYY-MM-DD): ")
    end_date = input_valid_date("Enter end date (YYYY-MM-DD): ")

    start_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_obj = datetime.strptime(end_date, "%Y-%m-%d")

    if start_obj > end_obj:
        print("Start date cannot be after end date.")
        return

    results = []
    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        if start_obj <= expense_date <= end_obj:
            results.append(expense)

    if len(results) == 0:
        print("No matching expenses found.")
        return

    print_expenses_table(results, f"EXPENSES FROM {start_date} TO {end_date}")


def sort_by_amount_ascending(expenses):
    print("\n=== SORT BY AMOUNT (ASCENDING) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["amount"])
    print_expenses_table(sorted_expenses, "SORTED BY AMOUNT ASCENDING")


def sort_by_amount_descending(expenses):
    print("\n=== SORT BY AMOUNT (DESCENDING) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["amount"], reverse=True)
    print_expenses_table(sorted_expenses, "SORTED BY AMOUNT DESCENDING")


def sort_by_category_a_to_z(expenses):
    print("\n=== SORT BY CATEGORY (A-Z) ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    sorted_expenses = sorted(expenses, key=lambda item: item["category"].lower())
    print_expenses_table(sorted_expenses, "SORTED BY CATEGORY A-Z")


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

    table = PrettyTable()
    table.field_names = ["Category", "Count", "Total Amount"]
    table.align["Category"] = "l"
    table.align["Count"] = "r"
    table.align["Total Amount"] = "r"

    category_totals = {}
    category_counts = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0
            category_counts[category] = 0

        category_totals[category] += expense["amount"]
        category_counts[category] += 1

    for category in sorted(category_totals.keys()):
        table.add_row([
            category,
            category_counts[category],
            f"{category_totals[category]:.2f}"
        ])

    print(table)


def update_expense(expenses):
    print("\n=== UPDATE EXPENSE ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    target_id = input("Enter exact expense ID to update: ").strip()
    index = find_expense_index_by_id(expenses, target_id)

    if index == -1:
        print("No expense found with that ID.")
        return

    print_expenses_table([expenses[index]], "CURRENT EXPENSE")

    print("\nEnter new data for this expense:")
    date = input_valid_date("Enter new date (YYYY-MM-DD): ")
    category = input_category("Enter new category: ")
    description = input_description("Enter new description: ")
    amount = input_positive_float("Enter new amount: ")

    expenses[index]["date"] = date
    expenses[index]["category"] = category
    expenses[index]["description"] = description
    expenses[index]["amount"] = amount

    save_expenses(DATA_FILE, expenses)
    print("Expense updated successfully.")


def delete_expense(expenses):
    print("\n=== DELETE EXPENSE ===")
    if len(expenses) == 0:
        print("No expenses found.")
        return

    target_id = input("Enter exact expense ID to delete: ").strip()
    index = find_expense_index_by_id(expenses, target_id)

    if index == -1:
        print("No expense found with that ID.")
        return

    print_expenses_table([expenses[index]], "EXPENSE TO DELETE")

    confirm = input("Are you sure you want to delete this expense? (y/n): ").strip().lower()
    if confirm == "y":
        del expenses[index]
        save_expenses(DATA_FILE, expenses)
        print("Expense deleted successfully.")
    else:
        print("Delete cancelled.")


def display_search_menu():
    print("\n" + "-" * 45)
    print("🔍 SEARCH MENU")
    print("-" * 45)
    print("1. Search by exact ID")
    print("2. Search by keyword")
    print("3. Search by amount range")
    print("4. Search by date range")
    print("0. Back to main menu")
    print("-" * 45)


def search_menu(expenses):
    while True:
        display_search_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_by_exact_id(expenses)
        elif choice == "2":
            search_by_keyword(expenses)
        elif choice == "3":
            search_by_amount_range(expenses)
        elif choice == "4":
            search_by_date_range(expenses)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter again.")


def display_sort_menu():
    print("\n" + "-" * 45)
    print("🔃 SORT MENU")
    print("-" * 45)
    print("1. Sort by amount ascending")
    print("2. Sort by amount descending")
    print("3. Sort by category A-Z")
    print("0. Back to main menu")
    print("-" * 45)


def sort_menu(expenses):
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
    print("\n" + "-" * 45)
    print("📊 STATISTICS MENU")
    print("-" * 45)
    print("1. Show basic statistics")
    print("2. Show statistics by category")
    print("0. Back to main menu")
    print("-" * 45)


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


def display_menu():
    print("\n" + "=" * 60)
    print("            💰 PERSONAL FINANCE / EXPENSE TRACKER")
    print("=" * 60)
    print("  1. ➕ Add new expense")
    print("  2. 📄 Display all expenses")
    print("  3. 🔍 Search")
    print("  4. 🔃 Sort")
    print("  5. 📊 Statistics")
    print("  6. ✏️ Update expense")
    print("  7. 🗑 Delete expense")
    print("  8. 📁 Export to JSON")
    print("  0. ❌ Exit")
    print("=" * 60)


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
            sort_menu(expenses)
        elif choice == "5":
            statistics_menu(expenses)
        elif choice == "6":
            update_expense(expenses)
        elif choice == "7":
            delete_expense(expenses)
        elif choice == "8":
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