from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = ""

engine = create_engine("postgresql+psycopg2://postgres:__enter_password__@localhost:5432/European")