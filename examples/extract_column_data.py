# examples/extract_column_data.py
import sqlite3

def extract_sample_data(conn, table, column):
    cursor = conn.cursor()
    cursor.execute(f"SELECT {column} FROM {table} LIMIT 1000")
    return [row[0] for row in cursor.fetchall()]
