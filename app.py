from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing employees
employees = [
    {'id': 1, 'name': 'Alice', 'position': 'Developer'},
    {'id': 2, 'name': 'Bob', 'position': 'Manager'},
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((emp for emp in employees if emp['id'] == id), None)
    return jsonify(employee) if employee else ('', 404)

@app.route('/employee', methods=['POST'])
def add_employee():
    new_employee = request.json
    employees.append(new_employee)
    return jsonify(new_employee), 201

if __name__ == '__main__':
    app.run(debug=True)