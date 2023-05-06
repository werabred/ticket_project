import mysql.connector as sql

with sql.connect(host="localhost", user="flask1", password="ubuntu", database="flask_db") as conn: 
    cur = conn.cursor()
    cmd = "select * from tickets"

    cur.execute(cmd)
    
    # lst = []
    # for item in cur:
    #     lst.append(item)

    # for item in lst:
    #     print(item)

    for item in cur:
        print(item)
