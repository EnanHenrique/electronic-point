from sqlalchemy.orm import Session

from repository.employee_repository import EmployeeRepository

class EmployeeService:

    @staticmethod
    def get_employees(db: Session, limit: int=100):
        return EmployeeRepository.get_employees(db, limit)

    @staticmethod
    def get_employees_join_records(db: Session, limit: int=100):
        return EmployeeRepository.get_employees_join_records(db, limit)
