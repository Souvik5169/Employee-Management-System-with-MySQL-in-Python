import mysql.connector
from mysql.connector import Error
from datetime import datetime
import logging
import os


# Logger Configuration
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(filename="logs/app.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


# DB Connection Manager
class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='yourpassword',
                database='company_db'
            )
            self.cursor = self.connection.cursor()
            logging.info("Database connected successfully.")
        except Error as e:
            logging.error(f"Error connecting to MySQL: {e}")
            raise

    def __del__(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            logging.info("Database connection closed.")


# Employee Operations
class EmployeeManager(DatabaseConnection):

    def add_employee(self, name, dept, salary, join_date):
        try:
            query = "INSERT INTO employees (name, department, salary, joining_date) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (name, dept, salary, join_date))
            self.connection.commit()
            logging.info(f"Added employee: {name}")
            print("Employee added successfully.\n")
        except Error as e:
            logging.error(f"Add employee failed: {e}")
            print("Failed to add employee.")

    def update_employee(self, emp_id, field, new_value):
        try:
            query = f"UPDATE employees SET {field} = %s WHERE id = %s"
            self.cursor.execute(query, (new_value, emp_id))
            self.connection.commit()
            logging.info(f"Updated employee {emp_id}'s {field} to {new_value}")
            print("Employee updated successfully.\n")
        except Error as e:
            logging.error(f"Update failed: {e}")
            print("Failed to update employee.")

    def delete_employee(self, emp_id):
        try:
            query = "DELETE FROM employees WHERE id = %s"
            self.cursor.execute(query, (emp_id,))
            self.connection.commit()
            logging.info(f"Deleted employee with ID {emp_id}")
            print("Employee deleted successfully.\n")
        except Error as e:
            logging.error(f"Delete failed: {e}")
            print("Failed to delete employee.")

    def view_all_employees(self):
        try:
            query = "SELECT * FROM employees"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            print("\n--- Employee Records ---")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: {row[3]}, Joined: {row[4]}")
            print("-------------------------\n")
            logging.info("Viewed all employee records.")
        except Error as e:
            logging.error(f"View failed: {e}")

    def search_employee_by_name(self, name):
        try:
            query = "SELECT * FROM employees WHERE name LIKE %s"
            self.cursor.execute(query, (f"%{name}%",))
            results = self.cursor.fetchall()
            print("\n--- Search Results ---")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: {row[3]}, Joined: {row[4]}")
            print("-----------------------\n")
            logging.info(f"Searched employees by name: {name}")
        except Error as e:
            logging.error(f"Search failed: {e}")


# Menu Handler
def menu():
    manager = EmployeeManager()
    while True:
        print("""
======== Employee Management System ========
1. Add Employee
2. Update Employee
3. Delete Employee
4. View All Employees
5. Search Employee
6. Exit
""")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Name: ")
            dept = input("Department: ")
            salary = float(input("Salary: "))
            join_date = input("Joining Date (YYYY-MM-DD): ")
            manager.add_employee(name, dept, salary, join_date)

        elif choice == '2':
            emp_id = int(input("Employee ID to update: "))
            field = input("Field to update (name/department/salary/joining_date): ")
            new_value = input("New value: ")
            if field == "salary":
                new_value = float(new_value)
            elif field == "joining_date":
                datetime.strptime(new_value, "%Y-%m-%d")
            manager.update_employee(emp_id, field, new_value)

        elif choice == '3':
            emp_id = int(input("Employee ID to delete: "))
            manager.delete_employee(emp_id)

        elif choice == '4':
            manager.view_all_employees()

        elif choice == '5':
            name = input("Enter name to search: ")
            manager.search_employee_by_name(name)

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


# Entry Point
if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        logging.critical(f"Critical error: {e}")
        print("An unexpected error occurred. Please check logs.")
