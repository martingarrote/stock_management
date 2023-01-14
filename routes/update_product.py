from general.config import *
from models.product import *
from general.tools import *

@app.route("/update_product/<int:product_id>", methods = ["PUT"])
def update_product(product_id):
    data = request.get_json()
    try:
        if product_id:
            product_target = Product.query.get(product_id)
            if data["validity"]:
                data["validity"] = date_format(data["validity"])
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
