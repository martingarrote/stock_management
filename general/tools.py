from general.config import *
from models.product import *
from hashlib import blake2b

# Transform data in json data
def to_json(data):
    """
    Receives don't json data and convert to json
    """
    result = []
    if type(data) is list:
        for i in data:
            result.append(i.json())
    else:
        result = data.json()
    return result

# Create an result message to routes
def new_result(result, details):
    """
    Receives the result and the details and generate a json answer
    """
    return jsonify({"result": result, "details": details})

# Return the result
def result_generator(class_name: str, data_list: list):
    """
    Receives a json list and return the sentence based on informed data
    """
    if len(data_list) == 0:
        return new_result("not found", f"the desired {class_name}s were not found")
    elif len(data_list) >= 1:
        return new_result("success", data_list)
    else:
        return new_result("error", "an unexpected error occurred")

# Receives non formated date and return formated date
def date_format(nf_date):
    """
    Takes a date and treats it to the desired format
    """
    part = nf_date.split("-")
    return date(int(part[0]), int(part[1]), int(part[2]))

# Encrypt password
def encrypt(password):
    h = blake2b()
    byted = bytes(password, encoding= "utf-8")
    h.update(byted)
    return h.hexdigest()

# Valid password provided
def validate_password(pw_encrypted, given_pw):
    given = encrypt(given_pw)
    if given == pw_encrypted:
        return True
    return False

# Verify if the user have permission to do certain thing
def can_do(route, method, permission):
    only_admin_routes = ["read_person", "update_person", "delete_person", "read_permissions"]
    worker = ["create", "read", "update"]

    if route.lower() in only_admin_routes:
        if permission.lower() == "admin":
            return True
    else:
        if permission.lower() == "admin":
            return True
        elif permission.lower() == "worker":
            if method.lower() in worker:
                return True
        elif permission.lower() == "default" and method.lower() == "read":
            return True
    return False