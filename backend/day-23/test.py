from flask import Flask, request, jsonify
# Flask is the main class of the Flask framework
# request is used to get the request data from the client
# jsonify is used to convert a dictionary into a JSON response

app = Flask(__name__)
# It creates a new Flask application instance

# Sample data (list of tasks)
tasks = []
# In real world, you will use a database to store the tasks

# Route to get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200

# Route to create a new task
# creating this need to go in the "Postman" or curl in the terminal or any other API testing tool
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' in data:
        task = {'title': data['title']}
        tasks.append(task)
        return jsonify({'message': 'Task created successfully'}, 201)
    else:
        return jsonify({'message': 'Title is required'}, 400)

# Route to update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
# <int:task_id> is a URL integer parameter, which is used to pass the task ID
# for the task_id, it is the index of the task in the tasks list
def update_task(task_id):
    if task_id < len(tasks):
        data = request.get_json()
        if 'title' in data:
            tasks[task_id]['title'] = data['title']
            return jsonify({'message': 'Task updated successfully'})
        else:
            return jsonify({'message': 'Title is required'}, 400)
    else:
        return jsonify({'message': 'Task not found'}, 404)

# Route to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
# <int:task_id> is a URL integer parameter, which is used to pass the task ID
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}, 404)

# a common practice to include this in Flask applications to run the app
if __name__ == '__main__':
    app.run()