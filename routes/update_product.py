from general.config import *
from models.product import *
from general.tools import *

@app.route("/update_product/<int:product_id>", methods = ["PUT"])
def update_product(product_id):
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
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

@app.route("/update_expired_products", methods = ["PUT"])
def update_expired_products():
    products = Product.query.filter(Product.validity < date.today()).all()
    expired_products = []
    for p in products:
        if p.expired == False:
            p.expired = True
            expired_products.append(p)

    db.session.commit()
    result = result_generator(to_json(expired_products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result