import redis
from flask import Flask,jsonify
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set("man","kalyanram")
app=Flask(__name__)
@app.route("/")
def func():
    return jsonify([
                    {"index":r.get("man")},
                    {"index":"poijkl"},
                    {"index":"kalyanert"},
                    {"index":"12345"},
                    {"index":r.get("kalyan")},

                    ]) 
if __name__=="__main__":
    app.run(port=4500)
print(dir(redis))