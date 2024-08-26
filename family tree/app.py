# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "stvrlight" # write your name
    age = "999999999999" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
    return render_tempelate('father.html',name = ummm)

# define the route to mother webpage
    return render_tempelate('mother.html',name = ame)

# define the route to friends webpage
    return render_tempelate('index.html',name = nme)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
