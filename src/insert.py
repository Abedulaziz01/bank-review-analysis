import csv
import os
from oracle_test import get_connection  # Import connection function

def insert_csv_to_table():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        print("Connected to Oracle Database.")

        csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', '../data/processed_reviews.csv')  # Adjust filename here

        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            insert_sql = """
                INSERT INTO bank_review (review, rating, review_date, bank, source, processed_review)
                VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6)
            """

            data_to_insert = []
            for row in reader:
                data_to_insert.append((
                    row['review'],
                    float(row['rating']) if row['rating'] else None,
                    row['date'],  # 'YYYY-MM-DD' format expected
                    row['bank'],
                    row['source'],
                    row['processed_review']
                ))

            cursor.executemany(insert_sql, data_to_insert)

        conn.commit()
        print(f"Inserted {cursor.rowcount} rows successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    insert_csv_to_table()
