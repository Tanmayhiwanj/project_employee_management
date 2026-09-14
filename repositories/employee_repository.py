import json
from pathlib import Path

from models.employee import Employee


class EmployeeRepository:

    def __init__(self, file_path: str = "data/employees.json"):
        self.file_path = Path(file_path)

    def load_all(self) -> dict[int, Employee]:

        if not self.file_path.exists():
            return {}

        with open(self.file_path, "r") as file:
            data = json.load(file)

        employees = {
            item["employee_id"]: Employee.from_dict(item)
            for item in data
        }

        return employees

    def save_all(self, employees: dict[int, Employee]) -> None:

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        data = [
            employee.to_dict()
            for employee in employees.values()
        ]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)