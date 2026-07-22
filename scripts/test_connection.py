from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
#load environment varibales from .env 
load_dotenv()
#read the connaction string
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL: 
    raise ValueError("DATABASE_URL not found in .env file")
#create engine (the interface between Python and the databse)
engine = create_engine(DATABASE_URL)
#connect and run a query 
with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    row = result.fetchone() 
    print("PostgreSQL version:", row[0])