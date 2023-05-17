import mysql.connector as sql

conn = sql.connect(host="localhost", user='flask1', password = "ubuntu")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE USER 'flask1'@'localhost' IDENTIFIED BY 'ubuntu';"
cur.execute(cmd)

cmd = "GRANT ALL PRIVILEGES ON *.* TO 'flask1'@'localhost' WITH GRANT OPTION;"
cur.execute(cmd)

cmd = "FLUSH PRIVILEGES;"
cur.execute(cmd)

conn.close()
