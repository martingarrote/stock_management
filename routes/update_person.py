from general.config import *
from general.tools import *
from models.person import *
from models.permission import *

@app.route("/update_person/<int:person_id>", methods = ["PUT"])
def update_person(person_id):
    data = request.get_json()
    try:
        if person_id:
            person_target = Person.query.get(person_id)
            for at in data:
                setattr(person_target, at, data[at])
            db.session.commit()
            result = new_result("success", "the person has been updated")
        else:
            result = new_result("error", "the id was not given")
    except Exception as e:
        result = new_result("error", str(e))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result