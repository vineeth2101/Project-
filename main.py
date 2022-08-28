from flask import Flask
from flask_cors import CORS, cross_origin
import sqlite3
from sqlCode import *
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    print("<<<<<<<<<<<<<<,,ddddddddddddddddd")
    ravl = {"msg":"ccccccccccccccc"}
    return rval

@app.route("/write")
def write():
    print("wwwwwwwwwwwwwwww")
    params = {"name":'raj',
          "age":21,
          "idno":"ddddddd"}
    ret = writeData(params)
    print("__________",ret)
    rval = {"msg":"ddddddddd"}
    return rval

@app.route("/read")
def read():
    print("rrrrrrrrrrrrrrr")
    ret = read_Data()
    print("rettttttttt",ret)
    rval = {"msg":ret}
    return rval


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
