import os
import MySQLdb
from flask import Flask

app = Flask(__name__)

db = MySQLdb.connect(
    host=os.getenv("DB_HOST", "db"),
    user=os.getenv("DB_USER", "root"),
    passwd=os.getenv("DB_PASSWORD", "password"),
    db=os.getenv("DB_NAME", "hospital_db")
    )
