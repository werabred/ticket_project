from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_student():
   return render_template('newticket.htm')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         empid = request.form['empid']
         empname = request.form['empname']
         empgender = request.form['empgender']
         empphone = request.form['empphone']
         empbdate = request.form['empbdate']
         
         with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employees (empid,empname,empgender,empphone,empbdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(empid,empname,empgender,empphone,empbdate)
            cur.execute(cmd)
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
         
      finally:
         return render_template("output.htm",msg = msg)
         con.close()

@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from employees")
      rows = cur.fetchall()

   return render_template("list.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
