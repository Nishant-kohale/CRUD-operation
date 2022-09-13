from flask import Flask, jsonify, request

app = Flask(__name__)
students =[
    {
        'id' : 1,
        'name' : 'Nishant Kohale',
        'department' : 'ETC'
    },
    {
        'id': 2,
        'name': 'Rahul',
        'department': 'CSE'
    },
    {
        'id': 3,
        'name': 'Pooja',
        'department': 'IT'
    }

]
@app.route('/')
def home():
    return "Hello"

### Create the sutdents details
@app.route('/student', methods=['POST'])
def create_student():
    request_data = request.get_json()
    new_student = {
        'id': request_data['id'],
        'name': request_data['name'],
        'department': request_data['department']
    }
    students.append(new_student)
    return jsonify(new_student)

### Get student name
@app.route('/student/<int:id>')
def get_student_name(id):
    for student in students:
        if(student['id'] == id):
            return jsonify(student)
    return jsonify({'message': 'store not found'})

### Get student info
@app.route('/student')
def get_all_student_name():
    return jsonify({'student_info': students})


# @app.route('/student/<string:name>/department', methods=['POST'])
# def create_store_item(name):
#     request_data = request.get_json()
#     for student in students:
#         if(student['name'] == name):
#             new_department = {
#                 'name': request_data['name'],
#                 'department': request_data['department']
#             }
#             student['department'].append(new_department)
#             return jsonify(new_department)
#     return jsonify({'message':'store not found'})


# @app.route('/student/<string:name>/department')
# def get_student_department(name):
#     for student in students:
#         if(student['name'] == name):
#             return jsonify(student['department'])
#     return jsonify({'message': 'store not found'})

## update student details
@app.route('/student/<int:id>',methods= ['PUT'])
def update_student(id):
    request_data = request.get_json()
    for student in students:
        if(student['id'] == id):
            new_student = {
                'name':request_data['name'],
                 'id': request_data['id'],
                'department': request_data['department']
            }

            students.append(new_student)
            return jsonify({'message': 'Data is de'})
    # return jsonify({'message': 'store not found'})


### delete student details
@app.route('/student/<int:id>',methods=['DELETE'])
def delete_student(id):
    for student in students:
        if(student['id'] == id):
            return jsonify(student)
    return jsonify({'message': 'Data is de'})
    # return jsonify((students['department']))






app.run(port=8000)