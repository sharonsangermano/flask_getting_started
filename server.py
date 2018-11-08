from flask import Flask, jsonify, request
import math
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    data = {
        "name": "Sharon",
    }
    return jsonify(data)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    data = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(data)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    p1 = r["a"]
    p2 = r["b"]
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    dis = math.sqrt(x**2 + y**2)
    data = {
        "distance": dis,
        "a": r["a"],
        "b": r["b"],
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
