from models.employee import Employee

from services.employee_service import EmployeeService

from repositories.employee_repository import EmployeeRepository

from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    EmployeeAlreadyExistsError
)


class EmployeeManagementApp:

    def __init__(self):

        repository = EmployeeRepository()

        self.service = EmployeeService(repository)

    def run(self):

        while True:

            self.display_menu()

            choice = input("Enter your choice: ").strip()

            try:

                if choice == "1":
                    self.add_employee()

                elif choice == "2":
                    self.view_all_employees()

                elif choice == "3":
                    self.find_employee()

                elif choice == "4":
                    self.update_salary()

                elif choice == "5":
                    self.change_department()

                elif choice == "6":
                    self.delete_employee()

                elif choice == "7":
                    self.search_employee()

                elif choice == "8":
                    print("Application closed.")
                    break

                else:
                    print("Invalid choice.")

            except (
                ValueError,
                EmployeeNotFoundError,
                EmployeeAlreadyExistsError
            ) as error:

                print(f"Error: {error}")

    @staticmethod
    def display_menu():

        print("\n")
        print("=" * 45)
        print("       EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Find Employee")
        print("4. Update Salary")
        print("5. Change Department")
        print("6. Delete Employee")
        print("7. Search Employee")
        print("8. Exit")

        print("=" * 45)

    def add_employee(self):

        print("\n--- Add Employee ---")

        employee_id = int(input("Employee ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        email = input("Email: ")
        department = input("Department: ")
        salary = float(input("Salary: "))

        employee = Employee(
            employee_id=employee_id,
            name=name,
            age=age,
            email=email,
            department=department,
            salary=salary
        )

        self.service.add_employee(employee)

        print("Employee added successfully.")

    def view_all_employees(self):

        print("\n--- All Employees ---")

        employees = self.service.get_all_employees()

        if not employees:
            print("No employees found.")
            return

        for employee in employees:
            self.display_employee(employee)

    def find_employee(self):

        print("\n--- Find Employee ---")

        employee_id = int(
            input("Enter employee ID: ")
        )

        employee = self.service.get_employee(employee_id)

        self.display_employee(employee)

    def update_salary(self):

        print("\n--- Update Salary ---")

        employee_id = int(
            input("Employee ID: ")
        )

        new_salary = float(
            input("New salary: ")
        )

        self.service.update_salary(
            employee_id,
            new_salary
        )

        print("Salary updated successfully.")

    def change_department(self):

        print("\n--- Change Department ---")

        employee_id = int(
            input("Employee ID: ")
        )

        department = input(
            "New department: "
        )

        self.service.change_department(
            employee_id,
            department
        )

        print("Department changed successfully.")

    def delete_employee(self):

        print("\n--- Delete Employee ---")

        employee_id = int(
            input("Employee ID: ")
        )

        self.service.delete_employee(
            employee_id
        )

        print("Employee deleted successfully.")

    def search_employee(self):

        print("\n--- Search Employee ---")

        print("1. Search by name")
        print("2. Search by department")

        choice = input("Choice: ").strip()

        if choice == "1":

            name = input("Enter name: ")

            employees = self.service.search_by_name(
                name
            )

        elif choice == "2":

            department = input(
                "Enter department: "
            )

            employees = self.service.search_by_department(
                department
            )

        else:

            print("Invalid choice.")
            return

        if not employees:

            print("No matching employees found.")
            return

        for employee in employees:
            self.display_employee(employee)

    @staticmethod
    def display_employee(employee: Employee):

        print("\n" + "-" * 40)

        print(f"ID         : {employee.employee_id}")
        print(f"Name       : {employee.name}")
        print(f"Age        : {employee.age}")
        print(f"Email      : {employee.email}")
        print(f"Department : {employee.department}")
        print(f"Salary     : ₹{employee.salary:,.2f}")

        print("-" * 40)


if __name__ == "__main__":

    app = EmployeeManagementApp()

    app.run()