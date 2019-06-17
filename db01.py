import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="postgres", host="172.16.66.244")
cur = conn.cursor()
# cur.execute("CREATE TABLE bugs (id serial PRIMARY KEY, name varchar(20),"
#             "cp int, hp int, dust int);")
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))


cur.execute("INSERT INTO test (name, cp, hp, dust) VALUES (%s, %s, %s, %s)",("ron", 100, 100, 100))
conn.commit()

# cur.execute("SELECT * FROM test;")
# result = cur.fetchone()

# print(result)