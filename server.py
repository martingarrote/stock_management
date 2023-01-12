from config import *
from tools import *
from product import *

# Search Types
# by name
# by price
# by perishable
# by freezable
# by validity

@app.route("/")
def server():
    return "Stock management"

# all products
@app.route("/products")
def list_products():
    products = db.session.query(Product).all()
    if len(products) == 0:
        result = new_result("not found", "don't have any product on database")
    else:
        result = new_result("success", to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# by name
@app.route("/products/search/<str:product_name>")
def searchby_name(product_name):
    products = Product.query.filter(Product.name.contains(product_name))
    if len(products) == 0:
        result = new_result("not found", "there are no products that meet the specified specifications on database")
    else:
        result = new_result("success", to_json(products))

app.run(debug = True)