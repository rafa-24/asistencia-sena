import psycopg2

def connect_database():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Rafael01242000',
        database='sena'
    )
    return connection