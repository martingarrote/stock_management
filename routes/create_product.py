from general.config import *
from models.product import *
from general.tools import *

@app.route("/new_product", methods= ["POST"])
def new_product():
    data = request.get_json()
    try:
        if data["validity"]:
            data["validity"] = date_format(data["validity"])
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        result = result_generator("product", to_json(product))
    except Exception as e:
        result = new_result("error", str(e))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# curl -d '{"name": "orange", "description": "orange fruit", "is_perishable": true, "freezable": false, "price": 0.40, "expired": false, "validity": "2023-01-17"}' -X POST -H "Content-Type:application/json" localhost:5000/new_product