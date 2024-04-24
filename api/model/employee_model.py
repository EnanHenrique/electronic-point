from sqlalchemy import Column, ForeignKey, BIGINT, VARCHAR
from sqlalchemy.orm import relationship

from config.database import Base_Electronic_Point
from model.record_model import Record

class Employee(Base_Electronic_Point):
    __tablename__ = "employee"

    id = Column(BIGINT, primary_key=True)
    name = Column(VARCHAR)
    job = Column(VARCHAR)

    records = relationship('Record', back_populates='employee')
