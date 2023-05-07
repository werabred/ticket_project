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

@app.route('/edit_ticket')
def edit_ticket():
   return render_template('modify.htm')

@app.route('/open')
def open():
   return render_template('opentickets.htm')

@app.route('/addrec', methods = ['POST'])
def addrec():
   if request.method == 'POST':
      try:
         apt = request.form['apt']
         urgency = request.form['urgency']
         room = request.form['room']
         perms = request.form['perms']
         problem = request.form['problem']
         status = "open"
         notes = "None"
         
         with sql.connect(host="localhost", user="flask1", password="ubuntu", database="tickets_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO tickets (apt,urgency,room,perms,problem,status,notes) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(apt,urgency,room,perms,problem,status,notes)
            cur.execute(cmd)
            
            con.commit()
            msg = "Ticket submitted. We will do our best to resolve your problem"
      except:
         con.rollback()
         msg = "There was an issue submitting your ticket. Please check that you filled all required fields (marked with *) and try again."
         
      finally:
         return render_template("output.htm",msg = msg)
         con.close()

#add notes to existing tickets
@app.route('/modify', methods = ['POST', 'GET'])
def modify():
   if request.method == 'POST':
      try:
         notes = request.form['notes']
         ticketid = request.form['ticketid']
         status = request.form['status']
         ticketid = int(ticketid)
         if notes == "":
            notes = "None"
         else:
            notes = notes

         with sql.connect(host="localhost", user="flask1", password="ubuntu", database="tickets_db") as con:
            cur = con.cursor()
            cmd = "update tickets set status = '{0}' where ticketid = {1}".format(status,ticketid)
            cur.execute(cmd)

            cmd = "update tickets set notes = '{0}' where ticketid = {1}".format(notes,ticketid)
            cur.execute(cmd)
            
            con.commit()
            msg = "Ticket updated."
      except:
         con.rollback()
         msg = "There was an issue updating the notes."
         
      finally:
         return render_template("output.htm", msg = msg)
         con.close()
@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask1", password="ubuntu", database="tickets_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from tickets")
      rows = cur.fetchall()
   return render_template("list.htm",rows = rows)
@app.route('/open_tickets')
def open_tickets():
   with sql.connect(host="localhost", user="flask1", password="ubuntu", database="tickets_db") as conn:  
      cur = conn.cursor()
      cur.execute("SELECT * FROM tickets WHERE status IN ('open', 'needs followup')")
      rows = cur.fetchall()
   return render_template("opentickets.htm", rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
