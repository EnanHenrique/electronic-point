from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Query
from typing import List

from schema.employee_schema import GetEmployeeSchema
from model.employee_model import Employee
from service.employee_service import EmployeeService
from config.get_db import get_db

app_router = APIRouter()

@app_router.get('/', status_code=200,
                # response_model=List[Employee]
                )
def get(
    db: Session = Depends(get_db),
    limit: int=Query(default=100)
    ):
    
    return EmployeeService.get_employees(db, limit)

@app_router.get('/records', status_code=200,
                # response_model=List[Employee]
                )
def get(
    db: Session = Depends(get_db),
    limit: int=Query(default=100)
    ):
    
    return EmployeeService.get_employees_join_records(db, limit)
