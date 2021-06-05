#This application demonstrates how to have web users submit form data directly to your mysql db through web form
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

app.config['SECRET_KEY'] = 'sdf5678990'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxxx'
app.config['db'] = 'flaskappdbproject'

mysql = MySQL(app)

#Form to enter name and email and department
@app.route('/', methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    if request.method == "POST":
        name=request.form['name']
        email=request.form['email']
        department=request.form['department']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO employee(employee_name,employee_email ) VALUES (%s, %s)", [name, email])
        cursor.execute("INSERT INTO department(department_name ) VALUES (%s)", [department])
        mysql.connection.commit()
        cursor.close()
        return 'Data Uploaded to Database'
    return render_template('form.html',form=form)


@app.route('/form')
def form():
    return render_template('form.html')

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.DataRequired()])
    department = TextField('Department:', validators=[validators.DataRequired()])
    email = TextField('Email:', validators=[validators.DataRequired()])


if __name__ == "__main__":
    app.run(debug=True)