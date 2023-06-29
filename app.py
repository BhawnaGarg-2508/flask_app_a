from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def hello_world2():
    return "<h1>This is about</h1>"

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "This is about input data from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
