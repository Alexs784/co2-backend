import sqlite3


def init_database():
    with open('schema.sql') as file:
        get_db_connection().executescript(file.read())


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def insert_co2_reading(value):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO co2_readings (value) VALUES (?)", [value])
    connection.commit()
    connection.close()


def get_latest_co2_readings():
    connection = get_db_connection()
    co2_readings = connection.execute("SELECT * FROM co2_readings LIMIT 100").fetchall()
    connection.close()
    return co2_readings
