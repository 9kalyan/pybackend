from flask import Flask,jsonify,request
import redis as rd
r = rd.Redis(host='red-ck5dggeru70s73buhagg', port=6379, decode_responses=True)
r.set('index', 'bar')
r.set('index','ram')
with open('ram.json') as kal:
    read=kal.read()
app=Flask(__name__)
title="kalyan"
@app.route("/",methods=['POST','GET'])
def func():
    global title
    if request.method=='POST':
        title = request.json['title']
        return title
    return jsonify([{"index":title}]) 
app.run(port=4500,host="0.0.0.0")