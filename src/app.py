from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label":"Mi primera tarea","done":False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position) #Esta vaina si pongo todos.remove funciona pero Learnpack dice que no
    todos_json = jsonify(todos)
    return todos_json

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)