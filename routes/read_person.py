from general.config import *
from general.tools import *
from models.person import *
from models.permission import *

@app.route("/persons")
def list_persons():
    persons = db.session.query(Person).all()
    result = result_generator("person", to_json(persons))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/persons/search/permission/<int:permission_id>")
def searchby_permission(permission_id):
    if permission_id > 3 or permission_id < 1:
        result = new_result("error", "invalid id")
    else:
        persons = Person.query.filter(Person.permission_id == permission_id).all()
        result = result_generator("person", to_json(persons))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/persons/search/id/<int:id>")
def searchby_person_id(id):
    persons = Person.query.get(id)
    result = result_generator("person", to_json(persons))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result