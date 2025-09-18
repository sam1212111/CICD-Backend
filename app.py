from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        tasks.append(task)
    return jsonify({"success": True})

# New DELETE route
@app.route('/tasks', methods=['DELETE'])
def delete_task():
    data = request.get_json()
    task = data.get('task')
    if task in tasks:
        tasks.remove(task)
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Task not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
