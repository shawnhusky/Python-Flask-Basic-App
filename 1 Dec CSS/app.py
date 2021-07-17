from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc



app = Flask(__name__)
app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


database1 = SQLAlchemy(app)

class shawnTable (database1.Model):
    _id = database1.Column(database1.Integer, primary_key=True)
    name = database1.Column(database1.String(100))
    email = database1.Column(database1.String(100))
    phone = database1.Column(database1.String(100))


def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone


#create table
@app.before_first_request
def create_tables():
    database1.create_all()
    
#routing

@app.route('/')
def Index(): 


    result = database1.session.query(shawnTable).all()
    #result = database1.Query.order_by(desc(shawnTable._id)).all()

   
    
    

    return render_template("index.html", passdata=result)

@app.route('/insert', methods=["POST", "GET"])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        u = shawnTable(name=name,email=email,phone=phone)
        database1.session.add(u)
        database1.session.commit()

        print(u.name)
    
    return render_template("insert.html")





if __name__ == "__main__":  
    app.run(debug=True)

