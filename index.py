from flask import Flask,jsonify
app=Flask(__name__)
@app.route("/")
def func():
    return jsonify([
                    {"index":"kalyan"},
                    {"index":"poijkl"},
                    {"index":"kalyanert"},
                    {"index":"12345"},
                    {"index":"1234"},

                    ]) 
app.run(port=4500)