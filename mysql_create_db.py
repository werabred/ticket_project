import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask1", password="ubuntu")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE DATABASE tickets_db"
cur.execute(cmd)
conn.close()

