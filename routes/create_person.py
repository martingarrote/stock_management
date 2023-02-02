from general.config import *
from general.tools import *
from models.person import *
from models.permission import *

@app.route("/create_person", methods = ["POST"])
def create_person():
    data = request.get_json()
    data["password"] = encrypt(data["password"])

    print(data)

    try:
        person = Person(**data)
        person.permission_id = 1
        db.session.add(person)
        db.session.commit()
        result = result_generator("person", to_json(person))
    except Exception as e:
        result = new_result("error", str(e))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result