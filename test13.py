from pathlib import Path

import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres",
                        password="postgres", host="172.16.66.244")

cur = conn.cursor()
try:
    cur.execute("SELECT * from test;")
    test = cur.fetchone()
    print(cur.fetchone())
    print(type(cur.fetchone()))
    print(type(test))
except AttributeError as e:
    print(e)
# print(test.fetchone())