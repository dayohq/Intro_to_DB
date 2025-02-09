import mysql.connector
from mysql.connector import Error

# Database credentials
db_host = "localhost"
db_user = "root"
db_password = "Ad@beTins"
db_name = "alx_book_store"

def create_database():
    """Function to create the database alx_book_store if it does not exist."""
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database {db_name} created successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Ensure connection is closed after operation
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()