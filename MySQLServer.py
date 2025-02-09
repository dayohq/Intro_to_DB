import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Update these credentials if necessary
        db_host = "localhost"
        db_user = "root"
        db_password = "Ad@beTins"
        db_name = "alx_book_store"

        # Attempt connection
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
            print(f"Database '{db_name}' created successfully!")
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure connection is properly closed
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()