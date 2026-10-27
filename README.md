![Library Management System Banner](https://capsule-render.vercel.app/api?type=waving&color=0:1D2671,100:C33764&height=200&section=header&text=Library%20Management%20System&fontSize=34&fontColor=ffffff&fontAlignY=40&desc=Python%20Project%20%7C%20Simple%20and%20Efficient&descAlignY=62&descSize=15)

<div align="center">

# 📚 Library Management System

### ✨ A Simple, Menu-Driven Library Management Application Using Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![Project](https://img.shields.io/badge/Project-Library%20Management-8A2BE2?style=for-the-badge&logo=bookstack)](https://github.com/)

**Manage books easily — add, search, issue, return, and view books!** 📖

</div>

---

## 🌟 About the Project

The **Library Management System** is a beginner-friendly Python project designed to manage basic library operations through a simple, menu-driven interface.

It allows users to display available books, add new books, search for a particular book, issue books, and return issued books. The project uses Python functions, lists, loops, conditional statements, and user input to perform different operations.

🎯 **Project Goal:** To understand the practical implementation of Python programming concepts by building a simple library management application.

## 🚀 Features

| Icon | Feature | Description |
|---|---|---|
| 📚 | Display Books | View the complete book list and its status. |
| ➕ | Add Books | Add new books to the library. |
| 🔍 | Search Books | Search for a book by its name. |
| 📤 | Issue Books | Issue a book if it is available. |
| 📥 | Return Books | Return a previously issued book. |
| ✅ | Status Tracking | Track books as Available or Issued. |
| 🛡️ | Input Validation | Check empty book names and invalid book numbers. |
| 🔄 | Interactive Menu | Select operations through a continuous menu. |

## 🛠️ Technologies Used

- 🐍 **Python 3** — Core programming language
- 📋 **Python Lists** — Store book names and their statuses
- ⚙️ **Functions** — Organize different library operations
- 🔁 **Loops** — Repeat the main menu and display books
- 🔀 **Conditional Statements** — Handle decisions and book status
- ⌨️ **User Input** — Accept choices and book names from the user

## 📂 Project Structure

```text
Library-Management-System/
│
├── Libraray management system.py
└── README.md
```

> 💡 Tip: You can rename your Python file to `library_management_system.py` to make it easier to run from the terminal.

## 💻 Getting Started

Follow these steps to run the project on your computer.

### 1️⃣ Install Python

Download and install Python 3 from the official website:

🔗 https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### 2️⃣ Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/Library-Management-System.git
```

### 3️⃣ Open the Project Folder

```bash
cd Library-Management-System
```

### 4️⃣ Run the Program

If you keep the original filename:

```bash
python "Libraray management system.py"
```

If you rename the file:

```bash
python library_management_system.py
```

🎉 That's it! Your Library Management System is ready to use.

## 🖥️ Sample Output

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. Display Books
2. Add Book
3. Search Book
4. Issue Book
5. Return Book
6. Exit

Enter your choice: 1

--- BOOK LIST ---
1 . Python Programming - Available
2 . Data Structures - Available
3 . Database Management - Available
```

### 📤 Example: Issuing a Book

```text
Enter your choice: 4

--- BOOK LIST ---
1 . Python Programming - Available
2 . Data Structures - Available
3 . Database Management - Available

Enter book number to issue: 1
Book issued successfully.
```

### 📥 Example: Returning a Book

```text
Enter your choice: 5

--- BOOK LIST ---
1 . Python Programming - Issued
2 . Data Structures - Available
3 . Database Management - Available

Enter book number to return: 1
Book returned successfully.
```

## 🧠 Python Concepts Demonstrated

This project helps beginners practice the following programming concepts:

- **Lists:** Store book information as nested lists.
- **Functions:** Use `display_books()`, `add_book()`, `search_book()`, `issue_book()`, and `return_book()`.
- **Loops:** Use `while` and `for` loops to control program execution.
- **Conditional Statements:** Use `if`, `elif`, and `else` to make decisions.
- **String Methods:** Use `.lower()` to search for book names without case sensitivity.
- **Boolean Variables:** Use `found` to determine whether a searched book exists.
- **List Methods:** Use `.append()` to add a new book.
- **Input and Output:** Use `input()` and `print()` to interact with users.

## 🔮 Future Enhancements

The project can be improved with additional functionality:

- 🗄️ Integrate a MySQL or SQLite database for permanent storage.
- 👤 Add user registration and login.
- 📅 Add issue dates and return deadlines.
- 💰 Calculate late-return fines.
- 📊 Generate library reports.
- 🖥️ Create a graphical user interface using Tkinter.
- 🔐 Add administrator and librarian roles.
- ⚠️ Improve error handling for non-numeric menu inputs.

## ⚠️ Current Limitations

- Book information is stored in a Python list and is lost when the program stops.
- The application runs in the terminal rather than a graphical interface.
- It does not include user accounts, due dates, or fine calculations.
- Invalid text entered where a number is expected may cause an error.

## 🎓 Learning Outcomes

By completing this project, I practiced Python fundamentals and learned how to combine multiple programming concepts into a working application.

This project strengthened my understanding of:

- Problem-solving and logical thinking.
- Function-based program design.
- Managing data with lists.
- Implementing real-world operations using conditional logic.
- Building an interactive, menu-driven program.

## 👩‍💻 Author

**Mahikdeep Kaur**

🎓 BCA (AI & ML) Student  
💻 Interested in Python Programming, Artificial Intelligence, and Machine Learning.

## 🤝 Contributing

Suggestions and improvements are welcome! Feel free to fork the repository and experiment with new features.

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## ⭐ Support

If you find this project useful for learning Python, consider giving the repository a ⭐ **Star** on GitHub!

---

<div align="center">

### 📚 Learn • Build • Improve • Repeat 🚀

**Made with ❤️ and Python 🐍**

</div>
