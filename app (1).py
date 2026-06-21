from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to REST API Fundamentals"
    })

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([
        {"id": 1, "name": "mekala"},
        {"id": 2, "name": "Student"}
    ])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json

    return jsonify({
        "message": "Student Added Successfully",
        "student": data
    })

if __name__ == '__main__':
    app.run(debug=True)