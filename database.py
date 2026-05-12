import sqlite3

def init_db():
    try:
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fname TEXT NOT NULL,
                    lname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL);
                    ''')
        conn.commit()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS user_logins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        login_time TEXT NOT NULL,
                       is_successful BOOLEAN NOT NULL,
                       FOREIGN KEY (user_id) REFERENCES users(id)
                       );
                       ''')
        conn.commit()
        conn.close()

        print("Database initialized successfully.")

    except sqlite3.Error as e:
        print(f"An error occured: {e}")


def add_first_user():
    try:
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute('''
                        INSERT INTO users (fname, lname, email, password)
                        VALUES ('John', 'Doe', 'john.doe@example.com', 'password123')
                        ''')
        conn.commit()
        conn.close()

        print("Added first users for testing.")

    except sqlite3.Error as e:
        print(f"An error occured: {e}")