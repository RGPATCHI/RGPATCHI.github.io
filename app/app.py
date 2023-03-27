from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compute_square', methods=['POST'])
def compute_square():
    num = request.json['num']
    square = int(num) ** 2
    return jsonify({'square': square})

if __name__ == '__main__':
    app.run()
