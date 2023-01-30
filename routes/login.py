from general.config import *
from general.tools import *
from models.person import *

@app.route("/login", methods = ["POST"])
def login():

    data = request.get_json()

    email = data["email"]
    pw = data["password"]

    person = Person.query.filter(Person.email == email, Person.password == encrypt(pw)).first()
    access_token = create_access_token(identity = email)

    if person is None:
        result = new_result("error", "email and/or password are incorrect")
    else:
        result = jsonify({"result": "success", "user": to_json(person), "token": access_token})
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result