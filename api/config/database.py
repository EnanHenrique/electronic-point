from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv

USER_DB = getenv('USER_DB')
PASSWD_DB = getenv('PASSWD_DB')
HOST_BD = getenv('HOST_BD')
SCHEMA_DB = getenv('SCHEMA_DB')
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER_DB}:{PASSWD_DB}@{HOST_BD}:3306/{SCHEMA_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine)

Base_Electronic_Point = declarative_base()
