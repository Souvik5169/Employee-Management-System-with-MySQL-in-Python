# 💼 Employee Management System (Python + MySQL)

A comprehensive **Employee Management System** built with Python and MySQL. This CLI-based project enables businesses to efficiently manage employee records including adding, updating, searching, and deleting employee data.

---

## 🚀 Features

- 🔐 Secure MySQL database operations using `mysql-connector-python`
- 🧠 Object-Oriented Design (OOP)
- 🔍 Search employee by name
- 📋 View all employee records
- 📝 Update specific fields (name, department, salary, joining date)
- 🗑️ Delete employees by ID
- 📁 Logs every operation in a file using Python’s `logging` module
- ⚠️ Robust error handling

---

## 🛠️ Tech Stack

| Tech             | Description                 |
|------------------|-----------------------------|
| Python 3.x       | Core application logic      |
| MySQL            | Backend database            |
| mysql-connector  | Python-MySQL communication  |
| logging module   | Activity logs               |

---

## 🏗️ Database Setup

Run the following SQL in your MySQL server:

```sql
CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(100),
    salary FLOAT,
    joining_date DATE
);
```

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/souvik5169/employee-management-system.git
cd employee-management-system
```

2. **Install dependencies**

```bash
pip install mysql-connector-python
```

3. **Update database credentials**

In `main.py`, update:

```python
self.connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='company_db'
)
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📂 Project Structure

```
employee-management-system/
│
├── main.py              # Main program
├── logs/
│   └── app.log          # Automatically generated logs
├── README.md            # Project info
```

---

## 👤 Author

**Souvik Kumar**  
🎓 Student at *Sainik School Purulia*  
🇮🇳 From *India*  
🔗 GitHub: [souvik5169](https://github.com/souvik5169)  
📧 Email: `cdtsouvikkumar@gmail.com`

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Support

If you found this project helpful, please consider leaving a ⭐️ on the repository.

---
