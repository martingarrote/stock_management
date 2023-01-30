from general.config import *
from general.tools import *
from models.person import *
from models.permission import *

@app.route("/persons")
@jwt_required()
def list_persons():
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("read_person", "get", user_permission):
        persons = db.session.query(Person).all()
        result = result_generator("person", to_json(persons))
    else:
        result = new_result("error", "insufficient error")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/persons/search/permission/<int:permission_id>")
@jwt_required()
def searchby_permission(permission_id):
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("read_person", "get", user_permission):
        if permission_id > 3 or permission_id < 1:
            result = new_result("error", "invalid id")
        else:
            persons = Person.query.filter(Person.permission_id == permission_id).all()
            result = result_generator("person", to_json(persons))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/persons/search/id/<int:id>")
@jwt_required()
def searchby_person_id(id):
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("read_person", "get", user_permission):
        persons = Person.query.get(id)
        result = result_generator("person", to_json(persons))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result