from general.config import *
from general.tools import *
from models.permission import *
from models.person import *

@app.route("/permissions")
@jwt_required()
def list_permissions():
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("read_permissions", "get", user_permission):
        permissions = db.session.query(Permission).all()
        result = result_generator("permission", to_json(permissions))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/permissions/search/id/<int:permission_id>")
@jwt_required()
def searchby_permission_id(permission_id):
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("read_permissions", "get", user_permission):
        permission = Permission.query.get(permission_id)
        result = result_generator("permission", to_json(permission))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result