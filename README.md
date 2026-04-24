# 💰 Personal Finance / Expense Tracker

## 📌 Overview
This is a **Command Line Interface (CLI)** application written in Python.

It helps users:
- Manage personal expenses
- Add, edit, delete records
- Search, sort, and analyze data
- Export data to JSON

---

## 🚀 Features

### 🔹 Basic Features
- ➕ Add new expense
- 📋 Display all expenses
- 🔍 Search by ID
- 🔃 Sort by amount
- 📊 Basic statistics:
  - Total expenses
  - Average expense
- 💾 Save & load data from `.txt`

---

### 🔹 Advanced Features
- 🔎 Advanced search (category, description, date)
- 🔀 Multiple sorting options
- 📈 Statistics by category
- 🗂 Export to `.json`
- ✏️ Update expense
- ❌ Delete expense

---

## 📂 Project Structure

- `expense_tracker.py`: Main program
- `expenses.txt`: Data storage
- `expenses.json`: Exported file
- `README.md`: Documentation

## 📄 Data Format

Stored in `expenses.txt`:

- Format: `id|date|category|description|amount`

### Example:

- `E01|2026-04-21|Food|Lunch|35000`
- `E02|2026-04-21|Transport|Bus ticket|10000`

---

## ▶️ How to Run

```bash
python expense_tracker.py
```

If not working:

```bash
python3 expense_tracker.py
```
## 🧠 Program Menu

```
💰 PERSONAL FINANCE / EXPENSE TRACKER

1. ➕ Add new expense
2. 📋 Display all expenses
3. 🔍 Search
4. 🔃 Sort
5. 📊 Statistics
6. ✏️ Update expense
7. ❌ Delete expense
8. 🗂 Export to JSON
0. ❌ Exit
```
## 🖥 Demo (Example Run)

Enter your choice: 1

=== ADD NEW EXPENSE ===  
Enter expense ID: E01  
Enter date: 2026-04-21  
Enter category: Food  
Enter description: Lunch  
Enter amount: 30000  

Expense added successfully!

🧩 Programming Concepts Used
Functions (modular design)
Loops (while True)
Conditional statements (if-elif)
File handling (.txt)
JSON handling
Data structures (list, dictionary)
🔄 Git Workflow
Create branch: topic4-expense-tracker
Make multiple commits
Push to GitHub
Create Pull Request
Merge into main
👨‍🎓 Author
Student: Nguyễn Võ Yên Khanh
Course: Programming Methods
