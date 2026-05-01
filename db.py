import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin@123.",  # put your MySQL password
        database="hospital_db"
    )