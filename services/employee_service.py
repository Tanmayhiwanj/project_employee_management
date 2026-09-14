from models.employee import Employee

from repositories.employee_repository import EmployeeRepository

from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    EmployeeAlreadyExistsError
)

from utils.validators import (
    validate_name,
    validate_age,
    validate_email,
    validate_department,
    validate_salary
)


class EmployeeService:

    def __init__(
        self,
        repository: EmployeeRepository
    ):
        self.repository = repository
        self.employees = self.repository.load_all()

    # -----------------------------
    # CREATE
    # -----------------------------

    def add_employee(self, employee: Employee) -> None:

        if employee.employee_id in self.employees:
            raise EmployeeAlreadyExistsError(
                f"Employee {employee.employee_id} already exists"
            )

        self._validate_employee(employee)

        self.employees[employee.employee_id] = employee

        self.repository.save_all(self.employees)

    # -----------------------------
    # READ
    # -----------------------------

    def get_employee(self, employee_id: int) -> Employee:

        employee = self.employees.get(employee_id)

        if employee is None:
            raise EmployeeNotFoundError(
                f"Employee {employee_id} not found"
            )

        return employee

    def get_all_employees(self) -> list[Employee]:

        return list(self.employees.values())

    # -----------------------------
    # UPDATE
    # -----------------------------

    def update_salary(
        self,
        employee_id: int,
        new_salary: float
    ) -> None:

        employee = self.get_employee(employee_id)

        validate_salary(new_salary)

        employee.update_salary(new_salary)

        self.repository.save_all(self.employees)

    def change_department(
        self,
        employee_id: int,
        new_department: str
    ) -> None:

        employee = self.get_employee(employee_id)

        validate_department(new_department)

        employee.change_department(new_department)

        self.repository.save_all(self.employees)

    # -----------------------------
    # DELETE
    # -----------------------------

    def delete_employee(self, employee_id: int) -> None:

        if employee_id not in self.employees:
            raise EmployeeNotFoundError(
                f"Employee {employee_id} not found"
            )

        del self.employees[employee_id]

        self.repository.save_all(self.employees)

    # -----------------------------
    # SEARCH
    # -----------------------------

    def search_by_name(
        self,
        name: str
    ) -> list[Employee]:

        return [
            employee
            for employee in self.employees.values()
            if name.lower() in employee.name.lower()
        ]

    def search_by_department(
        self,
        department: str
    ) -> list[Employee]:

        return [
            employee
            for employee in self.employees.values()
            if employee.department.lower() == department.lower()
        ]

    # -----------------------------
    # VALIDATION
    # -----------------------------

    @staticmethod
    def _validate_employee(employee: Employee) -> None:

        validate_name(employee.name)
        validate_age(employee.age)
        validate_email(employee.email)
        validate_department(employee.department)
        validate_salary(employee.salary)