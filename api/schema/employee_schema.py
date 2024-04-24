from pydantic import BaseModel

# from model.record_model import Record

class GetEmployeeSchema(BaseModel):
    class Config:
        from_attributes = True
        
    id: int
    name: str
    job: str

    records: list
