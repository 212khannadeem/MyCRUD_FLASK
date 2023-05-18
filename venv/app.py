from flask import Flask,render_template,request

import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enter_new_student')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
          nm = request.form['nm']
          addr = request.form['add']
          city = request.form['city']
          pin = request.form['pin']

          with sql.connect('database.db') as connection:
              
            cur=connection.cursor()

            cur.execute('INSERT INTO students(name, addr, city, pin) VALUES (?, ?, ?, ?)',(nm, addr, city, pin))

            connection.commit()

            msg="Record Successfully Added"

        except:
            connection.rollback() 
            msg="Error in insert operation"

        finally:
            return render_template('result.html', msg=msg)
            connection.close()
        
            
@app.route('/show_student')
def show_student():
    con=sql.connect('database.db')
    con.row_factory=sql.Row

    cur=con.cursor()

    cur.execute('SELECT * FROM students')

    rows=cur.fetchall()
    return render_template('show_list.html', rows=rows)

if __name__=='__main__':
    app.run(debug=True)