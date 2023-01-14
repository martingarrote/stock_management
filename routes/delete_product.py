from general.config import *
from models.product import *
from general.tools import *

@app.route("/delete_product/<int:product_id>", methods = ["DELETE"])
def delete_product(product_id):
    product_to_delete = Product.query.get(product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    result = new_result("success", f"the product with ID[{product_id}] has been deleted")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result