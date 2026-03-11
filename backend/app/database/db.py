import sqlite3

def get_db():
    conn = sqlite3.connect("proctoring.db")
    conn.row_factory = sqlite3.Row
    return conn