from general.config import *
from general.tools import *
from models.person import *

@app.route("/delete_person/<int:person_id>", methods = ["DELETE"])
def delete_person(person_id):
    person_to_delete = Person.query.get(person_id)
    db.session.delete(person_to_delete)
    db.session.commit()
    result = new_result("success", f"the product with ID[{person_id}] has been deleted")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result