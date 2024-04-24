from sqlalchemy.orm import Session, joinedload
from typing import List

from model.employee_model import Employee
from model.record_model import Record

class EmployeeRepository:

    @staticmethod
    def get_employees(db: Session, limit: int=100) -> List[Employee]:
        return db.query(Employee).limit(limit).all()

    @staticmethod
    def get_employees_join_records(db: Session, limit: int=100) -> List[Employee]:
        return db.query(Employee) \
        .join(Employee.records) \
        .limit(limit) \
        .options(joinedload(Employee.records)) \
        .all()
