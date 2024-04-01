import os
import mysql.connector as mysql
from dotenv import load_dotenv
load_dotenv()

def connectDB():
  HOST=os.getenv('HOST')
  USER=os.getenv('USER')
  PASSWORD=os.getenv('PASSWORD')
  DATABASE=os.getenv('DATABASE')
  
  try:
    db_cnn=mysql.connect(host=HOST,
                user=USER,
                passwd=PASSWORD,
                database=DATABASE)
    return db_cnn
  except Exception as e:
    return e