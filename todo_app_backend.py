import random
from flask import Flask, jsonify  # Import Flask and jsonify here

class ToDoBackend:
    def __init__(self):
        self.tasks = []

    # ... (backend logic)

# Create Flask app instance
app = Flask(__name__)
backend = ToDoBackend()  # Instantiate ToDoBackend outside of __main__

# API endpoint to get tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": backend.tasks})

# Other API endpoints for adding, deleting, etc.

if __name__ == "__main__":
    app.run()
