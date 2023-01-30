from general.config import *
from models.product import *
from general.tools import *
from models.person import *

@app.route("/delete_product/<int:product_id>", methods = ["DELETE"])
@jwt_required()
def delete_product(product_id):
    current_user = Person.query.filter(Person.email == get_jwt_identity()).first() 
    user_permission = current_user.permission.name
    if can_do("delete_product", "delete", user_permission):
        product_to_delete = Product.query.get(product_id)
        db.session.delete(product_to_delete)
        db.session.commit()
        result = new_result("success", f"the product with ID[{product_id}] has been deleted")
    else:
        result = new_result("error", "insufficient permission")
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result