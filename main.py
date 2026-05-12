import sqlite3
from database import init_db, add_first_user
from server import server

def main():
    # Print existing users in users database. Just for testing
    # try:
    #     conn = sqlite3.connect('example.db')
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT * FROM users')
    #     users = cursor.fetchall()
    #     for user in users:
    #         print(user)
    #     conn.close()

    # except sqlite3.Error as e:
    #     print(f"An error occured: {e}")    

    server()

if __name__ == "__main__":
    main()

