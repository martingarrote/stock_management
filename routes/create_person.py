from general.config import *
from general.tools import *
from models.person import *
from models.permission import *

@app.route("/create_person", methods = ["POST"])
@jwt_required()
def create_person():
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first()
    user_permission = current_user.permission.name
    if can_do("create_person", "post", user_permission):
        data = request.get_json()

        try:
            person = Person(**data)
            person.permission_id = 1
            db.session.add(person)
            db.session.commit()
            result = result_generator("person", to_json(person))
        except Exception as e:
            result = new_result("error", str(e))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result
