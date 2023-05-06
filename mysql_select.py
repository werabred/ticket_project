import mysql.connector as sql

with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as conn: 
    cur = conn.cursor()
    cmd = "select empid, empname, empgender, empphone, empbdate from employees"

    cur.execute(cmd)
    
    # lst = []
    # for item in cur:
    #     lst.append(item)

    # for item in lst:
    #     print(item)

    for item in cur:
        print(item)