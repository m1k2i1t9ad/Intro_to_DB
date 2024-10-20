import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',  # Change if necessary
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
