import psycopg

def connect():
    return psycopg.connect("host=127.0.0.1 dbname=phonebook user=postgres password=admeen")

def init_table(connection: psycopg.Connection):
    connection.execute("CREATE TABLE IF NOT EXISTS pb (username TEXT, phone TEXT PRIMARY KEY)")

def push(connection: psycopg.Connection, user: str, phone: str):
    connection.execute("INSERT INTO pb VALUES (%s, %s)", (user, phone))

def search(connection: psycopg.Connection, q: str):
    cursor = connection.execute("SELECT username, phone FROM pb WHERE to_tsvector(username || %s || phone) @@ websearch_to_tsquery(%s)", (' ', q)).fetchall()
    for row in cursor:
        yield row[0], row[1]
def all(connection: psycopg.Connection):
    cursor = connection.execute("SELECT * FROM pb")
    for row in cursor:
        yield row[0], row[1]

def delete(connection: psycopg.Connection, user: str):
    connection.execute("DELETE FROM pb WHERE username = %s", [user])