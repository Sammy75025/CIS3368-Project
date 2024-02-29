#Main File
print("Hello world")
import flask
from flask import jsonify
from flask import request
import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print("CONN SUCCESSFUL")
    except Error as e:
        print(f'the error {e} occured')
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occured")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result  = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' has occured")

conn = create_con('cis368spring.cb6eggewohwd.us-east-1.rds.amazonaws.com', 'admin','Yeager1001','cis3368springdb')
cursor = conn.cursor (dictionary = True)



