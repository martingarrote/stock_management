from general.config import *
from models.product import *

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
def result_generator(product_list: list):
    """
    Receives a json list and return the sentence based on informed data
    """
    if len(product_list) == 0:
        return new_result("not found", "the desired products were not found")
    elif len(product_list) >= 1:
        return new_result("success", product_list)
    else:
        return new_result("error", "an unexpected error occurred")

def date_format(nf_date):
    """
    Takes a date and treats it to the desired format
    """
    part = nf_date.split("-")
    return date(int(part[0]), int(part[1]), int(part[2]))