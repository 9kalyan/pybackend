from flask import Flask,jsonify
with open('ram.json') as kal:
    read=kal.read()
app=Flask(__name__)
@app.route("/")
def func():
    return jsonify([
                    {"index":"kalyanram"},
                    {"index":"poijkl"},
                    {"index":"kalyanert"},
                    {"index":"12345"},
                    {"index":"kalyan ram is excellent"},

                    ]) 
app.run(port=4500,host="0.0.0.0")