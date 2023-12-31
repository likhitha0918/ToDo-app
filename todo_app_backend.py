from flask import Flask, jsonify
from todo_app_backend import ToDoBackend

app = Flask(__name__)
backend = ToDoBackend()

# API endpoint to get tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": backend.tasks})

# Other API endpoints for adding, deleting, etc.

if __name__ == "__main__":
    app.run()
