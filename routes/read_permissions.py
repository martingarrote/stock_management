from general.config import *
from general.tools import *
from models.permission import *

@app.route("/permissions")
def list_permissions():
    permissions = db.session.query(Permission).all()
    result = result_generator("permission", to_json(permissions))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/permissions/search/id/<int:permission_id>")
def searchby_permission_id(permission_id):
    permission = Permission.query.get(permission_id)
    result = result_generator("permission", to_json(permission))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result