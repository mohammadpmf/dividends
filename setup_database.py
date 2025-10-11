import os
import pymysql
from pymysql import Error

def setup_database():
    """Create database and run migrations"""
    try:
        # Connect to MySQL
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='your_password'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS your_database_name")
            print("Database created or already exists")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    # Run migrations
    os.system('python manage.py migrate')
    # Create superuser if needed
    os.system('python manage.py createsuperuser --noinput')

if __name__ == '__main__':
    setup_database()