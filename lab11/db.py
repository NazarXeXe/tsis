import psycopg

def connect():
    return psycopg.connect("host=127.0.0.1 dbname=phonebook user=postgres password=admeen")

def init(connection: psycopg.Connection):
    connection.execute("CREATE TABLE IF NOT EXISTS pb (username TEXT PRIMARY KEY, phone TEXT)")

def push(connection: psycopg.Connection, user: str, phone: str):
    connection.execute("INSERT INTO pb VALUES (%s, %s)", (user, phone))

def replace(connection: psycopg.Connection, phone: str, by: str):
    connection.execute("UPDATE pb SET phone=%s WHERE username=%s", (phone, by))

def exist(connection: psycopg.Connection, username: str):
    return connection.execute("SELECT EXISTS(SELECT 1 FROM pb WHERE username=%s)", [username])

def search(connection: psycopg.Connection, q: str):
    cursor = connection.execute("SELECT username, phone FROM pb WHERE to_tsvector(username || %s || phone) @@ websearch_to_tsquery(%s)", (' ', q)).fetchall()
    for row in cursor:
        yield row[0], row[1]

def all(connection: psycopg.Connection):
    cursor = connection.execute("SELECT * FROM pb")
    for row in cursor:
        yield row[0], row[1]

def page(connection: psycopg.Connection, limit: int, offset: int):
    cursor = connection.execute("SELECT * FROM pb LIMIT %s OFFSET %s", (limit, offset*limit))
    for row in cursor:
        yield row[0], row[1]

def delete(connection: psycopg.Connection, user: str, phone: str):
    connection.execute("DELETE FROM pb WHERE username = %s OR phone= %s", [user, phone])
