from sqlalchemy import ForeignKey, Column, BIGINT, DATETIME
from sqlalchemy.orm import relationship

from config.database import Base_Electronic_Point

class Record(Base_Electronic_Point):
    __tablename__ = "record"

    id = Column(BIGINT, primary_key=True)
    date = Column(DATETIME)

    employee_id = Column(BIGINT, ForeignKey('employee.id'))
    employee = relationship('Employee', back_populates='records')
