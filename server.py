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
    return "Stock management is working"

# all products
@app.route("/products")
def list_products():
    products = db.session.query(Product).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# by name
@app.route("/products/search/name/<string:product_name>")
def searchby_name(product_name):
    products = Product.query.filter(Product.name.contains(product_name)).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# by price
@app.route("/products/search/price/<float:wanted_price>")
def searchby_price(wanted_price):
    products = Product.query.filter(Product.price.like(wanted_price)).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# max price
@app.route("/products/search/max_price/<float:max_price>")
def searchby_maxprice(max_price):
    products = Product.query.filter(Product.price < max_price).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# min price
@app.route("/products/search/min_price/<float:min_price>")
def searchby_minprice(min_price):
    products = Product.query.filter(Product.price > min_price).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# perishable
@app.route("/products/search/perishable/<int:value>")
def searchby_perishable(value):
    if value:
        products = Product.query.filter(Product.is_perishable == True).all()
    else:
        products = Product.query.filter(Product.is_perishable == False).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# freezable
@app.route("/products/search/freezable/<int:value>")
def searchby_freezable(value):
    if value:
        products = Product.query.filter(Product.freezable == True).all()
    else:
        products = Product.query.filter(Product.freezable == False).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

app.run(debug = True)