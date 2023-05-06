from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_ticket():
   return render_template('newticket.htm')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         apt = request.form['apt']
         urgency = request.form['urgency']
         room = request.form['room']
         perms = request.form['perms']
         problem = request.form['problem']
         file = request.form['file']
         
         with sql.connect(host="localhost", user="flask", password="ubuntu", database="tickets_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO tickets (apt,urgency,room,perms,problem,file) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(apt,urgency,room,perms,problem,file)
            cur.execute(cmd)
            
            con.commit()
            msg = "Ticket submitted. We will do our best to resolve your problem"
      except:
         con.rollback()
         msg = "There was an issue submitting your ticket. Please check that you filled all required fields (marked with *) and try again."
         
      finally:
         return render_template("output.htm",msg = msg)
         con.close()

@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask", password="ubuntu", database="tickets_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from tickets")
      rows = cur.fetchall()

   return render_template("list.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
