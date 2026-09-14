import re


def validate_name(name: str) -> None:
    if not name.strip():
        raise ValueError("Name cannot be empty")


def validate_age(age: int) -> None:
    if age < 18 or age > 100:
        raise ValueError("Age must be between 18 and 100")


def validate_email(email: str) -> None:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError("Invalid email address")


def validate_department(department: str) -> None:
    if not department.strip():
        raise ValueError("Department cannot be empty")


def validate_salary(salary: float) -> None:
    if salary <= 0:
        raise ValueError("Salary must be greater than 0")