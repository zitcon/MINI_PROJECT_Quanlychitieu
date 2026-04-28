💰 MINI PROJECT 3 - PERSONAL FINANCE / EXPENSE TRACKER
1. Project Description

This is a Python console application for managing personal expenses, built using procedural programming methods.

The program runs in a CLI (Command Line Interface) environment, allowing users to interact through a menu system.

It supports managing expenses including:

Adding, updating, deleting expenses
Searching and sorting data
Performing statistical analysis
Saving and loading data
Exporting structured data to JSON

This project was developed to apply knowledge from Programming Methods 1, including:

Using functions to modularize the program
Using loops for interactive menu
Using conditional statements for logic handling
Using lists and dictionaries for data storage
Validating user input
Reading and writing data to files
Formatting output into tables

Selected Topic: Personal Finance / Expense Tracker

2. Project Objective

The system is built with the following objectives:

Help users manage personal expenses efficiently
Allow adding, viewing, updating, and deleting records
Support searching and sorting for better usability
Provide statistical insights into spending behavior
Store data persistently using TXT files
Export structured data to JSON format
Practice procedural programming and clean code structure
3. Data Structure

Each expense is stored as a dictionary:

{
    "id": "E01",
    "date": "2026-04-21",
    "category": "Food",
    "description": "Lunch",
    "amount": 30000
}

The expense list is stored in a Python list:

expenses = [
    {...},
    {...}
]

👉 This structure makes it easy to search, sort, and analyze data.

4. Technologies Used
Component	Role
Python 3	Main programming language
TXT File (.txt)	Data storage
JSON File (.json)	Structured export
Git & GitHub	Version control
CLI	User interaction

No external libraries are required.

5. Project Structure
MINI_PROJECT_Quanlychitieu/
│-- expense_tracker.py
│-- expenses.txt
│-- expenses.json
│-- README.md
File	Function
expense_tracker.py	Main program
expenses.txt	Data storage
expenses.json	Exported data
README.md	Documentation
6. Main Features
6.1 Add New Expense

Users input:

ID (must start with E)
Date (not in the future)
Category (must be text)
Description
Amount (must be number)

👉 Includes input validation to prevent errors.

6.2 Display All Expenses

Displays all records in a formatted table.

6.3 Search Expense

Supports:

Search by exact ID
Search by keyword (substring)
Search by amount range
Search by date range
6.4 Sort Expenses

Supports:

Sort by amount ascending
Sort by amount descending
Sort by category
6.5 Statistics

Calculates:

Total expenses
Average expense
Highest expense
Lowest expense

👉 Advanced:

Statistics by category
6.6 Update Expense

Allows editing an existing expense by ID.

6.7 Delete Expense

Deletes an expense by ID.

6.8 Save & Load TXT
Automatically saves data
Loads data when program starts
6.9 Export to JSON

Exports all expenses to expenses.json.

7. Menu
PERSONAL FINANCE / EXPENSE TRACKER

1. Add new expense
2. Display all expenses
3. Search
4. Sort
5. Statistics
6. Update expense
7. Delete expense
8. Export to JSON
0. Exit
8. Input Validation
Data	Validation Rule
ID	Must start with "E"
Date	Cannot be in the future
Category	Must be text
Amount	Must be a number
9. Main Functions
Function	Role
add_expense()	Add new expense
display_expenses()	Show all expenses
search_expense()	Search data
sort_expense()	Sort data
statistics()	Calculate stats
update_expense()	Update record
delete_expense()	Delete record
export_json()	Export to JSON
main()	Control program
10. Usage Examples
Adding Expense
Enter ID: E01
Enter date: 2026-04-21
Enter category: Food
Enter description: Lunch
Enter amount: 30000
=> Expense added successfully
Statistics
Total expenses: 9
Average: 1823.00
Highest: 15000
Lowest: 2
11. Advanced Features
11.1 Keyword Search
Uses substring matching
Works on category & description
11.2 JSON Export
Exports structured data
Supports data sharing
12. How to Run
python expense_tracker.py

If not working:

python3 expense_tracker.py
13. Git Workflow
Create branch: topic4-expense-tracker
Make multiple commits
Push to GitHub
Create Pull Request
Merge into main
14. Self-Assessment
#	Component	Max	Score
1	CLI Menu	1	1
2	Input Validation	1	1
3	Data Display	1	1
4	Search	1	1
5	Sorting	1	1
6	Statistics	1	1
7	TXT File	1	1
8	Advanced Logic	1	1
9	JSON Export	1	1
10	Git & Code	1	1
TOTAL		10	10
15. Student Information
Student Name: Nguyễn Võ Yên Khanh
Course: Programming Methods
Project: Mini Project 3
