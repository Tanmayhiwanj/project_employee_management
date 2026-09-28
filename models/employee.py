from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: int
    name: str
    age: int
    email: str
    department: str
    salary: float

    def update_salary(self, new_salary: float) -> None:
        if new_salary <= 0:
            raise ValueError("Salary must be greater than 0")

        self.salary = new_salary

    def change_department(self, new_department: str) -> None:
        if not new_department.strip():
            raise ValueError("Department cannot be empty")

        self.department = new_department

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "salary": self.salary
        }
 # tanmay hiwanj is pushing code
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            employee_id=data["employee_id"],
            name=data["name"],
            age=data["age"],
            email=data["email"],
            department=data["department"],
            salary=data["salary"]
        )