from flask import Flask,render_template,request,redirect,url_for

import pymysql as sql

app = Flask(__name__)

def db_connect():
    db = sql.connect(host= 'localhost' , port=3306, user='root', password='', database = 'pydb')
    cursor = db.cursor()
    return db,cursor
    

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/afterlogin/", methods=['GET','POST'])
def afterlogin():
    if request.method == 'GET':
        return redirect(url_for("contact"))
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        db,cursor = db_connect()
        cmd = f"select * from user_data where email='{email}'"
        cursor.execute(cmd)
        data = cursor.fetchall()
        if data:
            msg = "Email already exist..."
            return render_template('contact.html', data=msg)
        else:
            cmd = f"insert into user_data values('{name}','{email}','{phone}','{message}')"
            cursor.execute(cmd)
            db.commit()
            db.close()
            msg = "Details are sent successfully..."
            return render_template('contact.html',data=msg)
    
    
        
    
app.run(debug=True)