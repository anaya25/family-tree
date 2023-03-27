# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Naina" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "Naveed" # write your name
    age = "38" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Angel" # write your name
    age = "36" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friends")
def home():

    name = "Anrua" # write your name
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
