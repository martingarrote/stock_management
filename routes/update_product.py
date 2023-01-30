from general.config import *
from models.product import *
from general.tools import *
from models.person import *

@app.route("/update_product/<int:product_id>", methods = ["PUT"])
@jwt_required()
def update_product(product_id):
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("update_product", "put", user_permission):
        data = request.get_json()
        try:
            if product_id:
                if "validity" in data:
                    if data["validity"] == "noValidity":
                        data["validity"] = None
                    else:
                        data["validity"] = date_format(data["validity"])
                product_target = Product.query.get(product_id)
                for at in data:
                    setattr(product_target, at, data[at])
                db.session.commit()
                result = new_result("success", "the product has been updated")
            else:
                result = new_result("error", "the id was not given")
        except Exception as e:
            result = new_result("error", str(e))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/update_expired_products", methods = ["PUT"])
@jwt_required()
def update_expired_products():
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("update_product", "put", user_permission):
        products = Product.query.filter(Product.validity < date.today()).all()
        expired_products = []
        for p in products:
            if p.expired == False:
                p.expired = True
                expired_products.append(p)

        db.session.commit()
        result = result_generator(to_json(expired_products))
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result