from flask import Flask,jsonify
import redis as rd
r = rd.Redis(host='red-ck5dggeru70s73buhagg', port=6379, decode_responses=True)
r.set('index', 'bar')
with open('ram.json') as kal:
    read=kal.read()
app=Flask(__name__)
@app.route("/")
def func():
    return jsonify([{"index":r.get('index')}]) 
app.run(port=4500,host="0.0.0.0")