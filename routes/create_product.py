from general.config import *
from models.product import *
from general.tools import *
from models.person import *

@app.route("/new_product", methods= ["POST"])
@jwt_required()
def new_product():
    
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first()
    user_permission = current_user.permission.name
    if can_do("create_product", "post", user_permission):
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
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# curl -d '{"name": "orange", "description": "orange fruit", "is_perishable": true, "freezable": false, "price": 0.40, "expired": false, "validity": "2023-01-17"}' -X POST -H "Content-Type:application/json" localhost:5000/new_product