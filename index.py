from flask import Flask,jsonify
import redis as rd
r = rd.Redis(host='red-ck5dggeru70s73buhagg', port=6379, decode_responses=True)
r.set('index', 'bar')
r.set('index','ram')
with open('ram.json') as kal:
    read=kal.read()
app=Flask(__name__)
@app.route("/",methods=['POST','GET'])
def func():
    if request.method=='POST':
        rd=request.get_json()
        kal=rd['index']
    return jsonify([{"index":kal}]) 
app.run(port=4500,host="0.0.0.0")