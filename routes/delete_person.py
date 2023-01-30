from general.config import *
from general.tools import *
from models.person import *

@app.route("/delete_person/<int:person_id>", methods = ["DELETE"])
@jwt_required()
def delete_person(person_id):
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("delete_person", "delete", user_permission):
        person_to_delete = Person.query.get(person_id)
        db.session.delete(person_to_delete)
        db.session.commit()
        result = new_result("success", f"the product with ID[{person_id}] has been deleted")
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result