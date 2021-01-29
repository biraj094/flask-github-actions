
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world"


def add(x,y):
	return x+y

if __name__=="__main__":
	app.run()
