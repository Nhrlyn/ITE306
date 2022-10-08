from flask import Flask
from flask import jsonify
from flask import request

app = flask (_name_)
empDB=[{'id':'101',
        'name':'Dorry',
        'title':'techno'},
       {'id':'102',
        'name':'barbie',
        'title':'software'}]

@app.route("/")
def hello():
    return"Hello word!"

@app.route('/empdb/employee/',method=['GET'])
def getAllEmp():
    return jsonify({'emp':empDB})

@app.route('/empdb/employee/<empId>',method=['GET'])
def getEmp(empId):
    usr = [emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emp':usr})

if _name_ == '_main_':
    app.run()