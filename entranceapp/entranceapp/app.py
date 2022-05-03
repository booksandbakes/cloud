from flask import Flask, render_template, redirect, url_for, request
import sqlalchemy as db
import pymysql
import mysql.connector
import json
import mysql.connector
from flaskext.mysql import MySQL

app = Flask(__name__)

# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'janet'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'mypassword'
# app.config['MYSQL_DATABASE_DB'] = 'entrance_db'
# app.config['MYSQL_DATABASE_HOST'] = 'db'

#'host':'root',
# mysql.init_app(app)
# conn = mysql.connect()

config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }
conn = mysql.connector.connect(**config)
with open("init.sql", 'r') as file1:
    sql_cmds = file1.read()

sql_cmds1 = sql_cmds.split(";")

for i in range(0, len(sql_cmds1)-1):
    query = sql_cmds1[i] + ';'
    cursor = conn.cursor()
    cursor.execute(query)
conn.commit()


@app.route('/', methods=['GET', 'POST'])
def index():

    error = None
    if request.method == 'POST':
        if request.form['submit_button'] == "signup":
            return redirect(url_for('signup'))
        else:
            return redirect(url_for('login'))
    return render_template('index.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }
    error = None
    if request.method == 'POST':
        if request.form['name'] == '' or request.form['password'] == '':
            error = "Fields can't be empty"
        else:
            
            con = mysql.connector.connect(**config)
            print('Connection successful\n')
            email = request.form['email']
            password = request.form['password']
            score=0
            name = request.form['name']
            cursor = con.cursor()
            # cursor.execute("INSERT INTO students values email='" + email + "' and password='" + password + "'")
            cursor.execute("""INSERT INTO students(email, password, name, score) VALUES (%s,%s,%s,%s)""", 
                            (email, password, name, score))
            con.commit()
            cursor.close()
            con.close()
            return redirect(url_for('index'))

    return render_template('signup.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():

    config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }

    error = None
    if request.method == 'POST':
        con = mysql.connector.connect(**config)
        email = request.form['email']
        password = request.form['password']
        cursor = con.cursor()
        cursor.execute("SELECT * from students where email='" + email + "' and password='" + password + "'")

        results = cursor.fetchone()
        cursor.close()
        con.close()

        if results is None:
            error = 'Invalid Credentials. Please try again.'      
        else:
            url_func='quiz/'+email
            return redirect(url_for('quiz', email=email))
    return render_template('login.html', error=error)


@app.route('/login_course', methods=['GET', 'POST'])
def login_course():

    config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }

    error = None
    if request.method == 'POST':
        con = mysql.connector.connect(**config)
        email = request.form['email']
        password = request.form['password']
        cursor = con.cursor()
        cursor.execute("SELECT * from students where email='" + email + "' and password='" + password + "'")

        results = cursor.fetchone()
        cursor.close()
        con.close()

        if results is None:
            error = 'Invalid Credentials. Please try again.'      
        else:
            return redirect(url_for('courses', email=email))
    return render_template('login.html', error=error)



@app.route('/end', methods=['GET', 'POST'])
def end():
    return render_template('end.html')

@app.route('/quiz/<email>', methods=['GET', 'POST'])
def quiz(email):

    config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }
    

    error = None
    con = mysql.connector.connect(**config)        
    cursor = con.cursor()
    cursor.execute("SELECT * FROM questions")

    results = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] 
    json_data=[]

    for result in results:
        json_data.append(dict(zip(row_headers,result)))
    if request.method == 'POST':
        
        answer_list=[request.form['ans0'], request.form['ans1'], request.form['ans2'], request.form['ans3'], request.form['ans4'], request.form['ans5']]
        score=0
        for i in range(len(answer_list)):
            if answer_list[i]=="option1" and json_data[i]['answer']==1:
                score+=1
            elif answer_list[i]=="option2" and json_data[i]['answer']==2:
                score+=1
            elif answer_list[i]=="option3" and json_data[i]['answer']==3:
                score+=1
            elif answer_list[i]=="option4" and json_data[i]['answer']==4:
                score+=1

        sql_cmd = "UPDATE students SET score=%s WHERE email=%s"
        sql_val = (score, email)
        cursor.execute(sql_cmd, sql_val)
        con.commit()
        cursor.close()
        con.close()
        # return "The test has ended"
        return str(score)+" "+email
        
    return render_template('quiz.html', ques_ans=json_data)


@app.route('/courses/<email>', methods=['GET', 'POST'])
def courses(email):

    config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }

    error = None
    con = mysql.connector.connect(**config)        
    cursor = con.cursor()
    cursor.execute("SELECT * FROM courses")

    results = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] 
    json_data=[]

    for result in results:
        json_data.append(dict(zip(row_headers,result)))
    if request.method == 'POST':
        course_option=request.form['course_option']
        if course_option=="option2":
            course_name=json_data[1]['course_name']
        elif course_option=="option3":
            course_name=json_data[2]['course_name']
        elif course_option=="option4":
            course_name=json_data[3]['course_name']
        else:
            course_name=""
        sql_cmd = "UPDATE students SET course_name=%s WHERE email=%s"
        sql_val = (course_name, email)
        cursor.execute(sql_cmd, sql_val)
        con.commit()
        cursor.close()
        con.close()
        return "REGISTERED"+course_name
    return render_template('courses.html', courses_list=json_data)

@app.route('/results', methods=['GET', 'POST'])
def results():

    config = {
    'user':'root',
    'password':'admin',
    'database':'entrance_db',
    'port' : '3306'
    }

    error = None
    con = mysql.connector.connect(**config)        
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students ORDER BY SCORE DESC")

    results = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] 
    json_data=[]

    for result in results:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    con.close()
    return json.dumps(json_data)

if __name__=="__main__":
    app.run(debug=True)