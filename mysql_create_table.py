import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="tickets_db")
cur = conn.cursor()

cmd = "CREATE TABLE tickets (\
    ticketid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    apt VARCHAR(255) NOT NULL,\
    urgency VARCHAR(255) NOT NULL, \
    room VARCHAR(255) NOT NULL, \
    perms VARCHAR(255) NOT NULL, \
    problem TEXT NOT NULL, \
    file FILESTREAM, \
    Resolved? bit )"

cur.execute(cmd)
conn.close()



