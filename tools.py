from config import *
from product import *

# Transform data in json data
def to_json(data):
    result = []
    for i in data:
        result.append(i.json())
    return result

# Create an result message to routes
def new_result(result, details):
    return jsonify({"result": result, "details": details})