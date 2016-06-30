# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, withic returns a string
def hello_world():
	return "Hello, World!"

# start the development server using the run()method
if __name__ == "__main__":
	app.run()
	