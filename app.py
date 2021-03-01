from flask import Flask, render_template, jsonify, request
import time
from jetbot import Robot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    if data == 38 :
        robot.forward(0.2)
    elif data == 39 :
        robot.right(0.2)
    elif data == 40 :
        robot.backward(0.2)
    elif data == 37 :
        robot.left(0.2)
    else :
        robot.stop()

    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6974, debug=True)
    