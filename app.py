# import the flask class
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# create an instance of the flask class 
app=Flask(__name__)
# define the route() decorator to link with a valid URL in the application


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:1812sasha2001@localhost:5432/increase")
db = SQLAlchemy(app)

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(80), unique=True)
#   email = db.Column(db.String(120), unique=True)

#   def __init__(self, username, email):
#     self.username = username
#     self.email = email

#   def __repr__(self):
#     return '<User %r>' % self.username

# @app.route('/') 
# # define a function that is triggered when this URL appears in the browser address bar
# def index(): 
#   # return something when this function is called 
#     return "Welcome to your Python Flask Website" 
    
db = scoped_session(sessionmaker(bind=engine))

app.secret_key = '12345678'
#Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route('/')
def main():    
    return render_template("addbook.html")
if __name__ == "__main__":                           
    app.run(host='0.0.0.0', debug=True, port=5050)

@app.route("/bookList")
def booklist():
  books=db.execute("SELECT * FROM booklist order by bookid")
  return render_template("bookList.html", books=books)

# @app.route("/bookadd", methods=["POST"])
# def bookadd():
#     money=request.form.get("money")

#     db.execute("INSERT INTO test (money) VALUES (:money)",
#             {"money": money}) 
#     db.commit() 
#     return render_template("addbook.html")

@app.route("/bookadd", methods=["POST"])
def bookadd():
    isbn=request.form.get("isbn")
    title=request.form.get("title")
    author=request.form.get("author")
    year=request.form.get("year")
    db.execute("INSERT INTO booklist (isbn, title,author, year) VALUES (:isbn, :title,:author,:year)",
            {"isbn": isbn, "title": title, "author":author,"year":year}) 
    db.commit() 
    return render_template("addbook.html")