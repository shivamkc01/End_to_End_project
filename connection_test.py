import pymysql
import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')



def check_database_existence(host, user, password, db_name):
    try:
        # Establish a connection to the MySQL server
        db = pymysql.connect(host=host, user=user, password=password)
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Execute the SQL query
        cursor.execute("SHOW DATABASES;")
        
        # Fetch all the rows
        databases = cursor.fetchall()
        
        # Check if the database exists
        if (db_name,) in databases:
            print(f"The database '{db_name}' exists.")
        else:
            print(f"The database '{db_name}' does not exist.")
            
    except pymysql.Error as e:
        print(f"Error occurred: {e}")
        
    finally:
        # Close the database connection
        if db:
            db.close()

# Replace 'your_host', 'your_user', 'your_password' with your actual MySQL server's host, user, and password
check_database_existence('localhost', 'root', 'Shivam123@', 'college_students')
