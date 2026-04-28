# 💰 **MINI PROJECT 3 - PERSONAL FINANCE / EXPENSE TRACKER**

---

## 📌 **1. Project Description**
This is a *Python console application* built using **procedural programming**.

The program runs in a **CLI (Command Line Interface)** environment and allows users to:
- Manage personal expenses  
- Add, update, delete records  
- Search, sort, and analyze data  
- Export data to **JSON**

---

## 🎯 **2. Project Objective**
The system is designed to:
- Help users manage expenses effectively  
- Practice *procedural programming*  
- Apply concepts like:
  - Functions  
  - Loops  
  - Conditionals  
  - File handling  

---

## 🧩 **3. Data Structure**

Each expense is stored as a **dictionary**:

```python
{
    "id": "E01",
    "date": "2026-04-21",
    "category": "Food",
    "description": "Lunch",
    "amount": 30000
}
The data is stored in a list:
expenses = [{...}, {...}]
## ⚙️ **4. Technologies Used**

| **Component** | **Role** |
|--------------|---------|
| **Python 3** | Main programming language |
| **TXT File (.txt)** | Data storage |
| **JSON File (.json)** | Structured data export |
| **Git & GitHub** | Version control |
| **CLI** | User interaction |

---

## 📂 **5. Project Structure**
expense_tracker.py # Main program
expenses.txt # Data storage
expenses.json # Exported file
README.md # Documentation

---

## 🚀 **6. Main Features**

### 🔹 **6.1 Add New Expense**
- **ID** must start with `E`  
- **Date** must be valid (*not in the future*)  
- **Category** must be text  
- **Amount** must be a number  

---

### 🔹 **6.2 Display Expenses**
- Show all data in **formatted table**

---

### 🔹 **6.3 Search**
- 🔍 Search by **ID**  
- 🔎 Search by *keyword*  
- 💰 Search by *amount range*  

---

### 🔹 **6.4 Sort**
- 🔃 Sort ascending  
- 🔃 Sort descending  
- 🔤 Sort by category  

---

### 🔹 **6.5 Statistics**
- 📊 Total expenses  
- 📈 Average expense  
- 🔺 Highest expense  
- 🔻 Lowest expense  

---

### 🔹 **6.6 Update & Delete**
- ✏️ Update existing expense  
- ❌ Delete expense by ID  

---

### 🔹 **6.7 Export JSON**
- 🗂 Export data to `expenses.json`  

---

## 🧠 **7. Menu**
PERSONAL FINANCE / EXPENSE TRACKER

1.Add new expense
2.Display all expenses
3.Search
4.Sort
5.Statistics
6.Update expense
7.Delete expense
8.Export to JSON
9.Exit

---

## ▶️ **8. How to Run**

```bash
python expense_tracker.py
## 🔄 **9. Git Workflow**

The project follows a structured **Git workflow**:

1. Create branch: `topic4-expense-tracker`  
2. Commit changes  
3. Push to GitHub  
4. Create Pull Request  
5. Merge into **main**  

---

## 📌 **10. Commit History Explanation**

| **Commit Name** | **Description** | **Purpose** |
|----------------|----------------|-------------|
| **Initial commit** | Create project structure | Set up base project |
| **Create initial expense tracker CLI** | Build menu and basic features | Establish core functionality |
| **Add advanced search sort statistics and JSON export** | Add advanced features | Extend functionality beyond requirements |
| **Fix date validation and input handling** | Improve input validation | Prevent invalid data |
| **Merge pull request** | Merge branch into main | Complete development workflow |
| **Update README.md** | Improve documentation | Make project more professional |
| **Final clean version** | Clean and finalize code | Prepare for submission |

---

## 📊 **11. Self-Assessment**

| **Criteria** | **Max Score** | **Your Score** |
|-------------|--------------|---------------|
| CLI Menu System | 1.0 | 1.0 |
| Input Validation | 1.0 | 1.0 |
| Data Display | 1.0 | 1.0 |
| Search Function | 1.0 | 1.0 |
| Sorting | 1.0 | 1.0 |
| Statistics | 1.0 | 1.0 |
| TXT File Handling | 1.0 | 1.0 |
| Advanced Logic | 1.0 | 1.0 |
| JSON Export | 1.0 | 1.0 |
| Git & Code Structure | 1.0 | 1.0 |
| **TOTAL** | **10.0** | **10.0** |

---

## 👨‍🎓 **12. Author**

- **Student:** Nguyễn Võ Yên Khanh  
- **Course:** *Programming Methods*  
- **Project:** *Mini Project 3 - Expense Tracker*  

