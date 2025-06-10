import oracledb
import os
import os

def get_connection():
    return oracledb.connect(
        user="sys",
        password="123",
        dsn="localhost:1521/XE",
        mode=oracledb.SYSDBA
    )

def create_table():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql_path = os.path.join(os.path.dirname(__file__), 'a.sql')
        with open(sql_path, 'r') as f:
            sql = f.read()

        cursor.execute(sql)
        conn.commit()
        print("Table created successfully.")

    except oracledb.DatabaseError as e:
        error_obj = e.args[0]
        if error_obj.code == 955:
            print("Table already exists, skipping creation.")
        else:
            print(f"Oracle Error {error_obj.code}: {error_obj.message}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table()
