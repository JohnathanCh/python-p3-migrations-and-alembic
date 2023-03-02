from datetime import datetime
from sqlalchemy import create_engine, desc, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    # id name email grade birthday enrolled_date
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())
    
    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"