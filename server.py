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
@app.route("/products/search/name/<string:product_name>")
def searchby_name(product_name):
    products = Product.query.filter(Product.name.contains(product_name)).all()
    if len(products) == 0:
        result = new_result("not found", "there are no products that meet the specified specifications on database")
    else:
        result = new_result("success", to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# by price
@app.route("/products/search/price/<float:wanted_price>")
def searchby_price(wanted_price):
    products = Product.query.filter(Product.price.like(wanted_price)).all()
    if len(products) == 0:
        result = new_result("not found", "there are no products that meet the specified specifications on database")
    else:
        result = new_result("success", to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# max price
@app.route("/products/search/max_price/<float:max_price>")
def searchby_maxprice(max_price):
    products = Product.query.filter(Product.price < max_price).all()
    if len(products) == 0:
        result = new_result("not found", "there are no products that meet the specified specifications on database")
    else:
        result = new_result("success", to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# min price
@app.route("/products/search/min_price/<float:min_price>")
def searchby_minprice(min_price):
    products = Product.query.filter(Product.price > min_price).all()
    if len(products) == 0:
        result = new_result("not found", "there are no products that meet the specified specifications on database")
    else:
        result = new_result("success", to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

#perishable
@app.route("/products/search/perishable/<int:value>")
def searchby_perishable(value):
    if value:
        products = Product.query.filter(Product.is_perishable == True).all()
    else:
        products = Product.query.filter(Product.is_perishable == False).all()
    if len(products) == 0:
        result = new_result("not found", "there are no products that meet the specified specifications on database")    
    else:
        result = new_result("success", to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

app.run(debug = True)