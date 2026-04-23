# Personal Finance / Expense Tracker

## 📌 Overview
This project is a Command Line Interface (CLI) application written in Python.  
It is designed to help users manage personal expenses, including adding, searching, sorting, and analyzing expense data.

The project follows **procedural programming principles** and meets all requirements of the Mini Project.

---

## ⚙️ Features

### 🔹 Basic Features
- Add new expense records
- Display all expenses in a formatted table
- Search expense by exact ID
- Sort expenses by amount
- Calculate basic statistics:
  - Total expenses
  - Average expense
- Save and load data from `.txt` file

---

### 🔹 Advanced Features
- Search by keyword (category, description, date)
- Sort by multiple options:
  - Ascending / Descending
  - Category (A → Z)
- Statistics by category (grouping data)
- Export data to `.json` file

---

## 📂 Project Structure
```text
expense_tracker.py   # Main program
expenses.txt         # Data storage (text file)
expenses.json        # Exported JSON file
README.md            # Project documentation
```

---

## 📄 Data Format

Data is stored in `expenses.txt` with the format:

```text
id|date|category|description|amount
```

### Example:

```text
E01|2026-04-21|Food|Lunch|35000
E02|2026-04-21|Transport|Bus ticket|10000
```

---

## ▶️ How to Run

Open terminal in project folder and run:

```bash
python expense_tracker.py
```

If it doesn't work:

```bash
python3 expense_tracker.py
```

---

## 📋 Menu

```text
1. Add new expense
2. Display all expenses
3. Search
4. Sort
5. Statistics
6. Export to JSON
0. Exit
```

---

## 🧠 Programming Concepts Used
- Functions (modular design)
- Loops (`while True`)
- Conditional statements (`if-elif`)
- File handling (`.txt`)
- JSON handling
- Data structures (list, dictionary)

---

## 📊 Git Workflow
- Create branch: `topic4-expense-tracker`
- Multiple commits (logical steps)
- Pull request & merge to `main`

---

## 👤 Author
- Student: **(Nguyễn Võ Yên Khanh)**
- Course: Programming Methods
