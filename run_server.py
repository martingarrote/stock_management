from general.config import *
from models.product import *
from general.tools import *

from routes.create_product import *
from routes.read_product import *
from routes.update_product import *
from routes.delete_product import *

from routes.create_person import *
from routes.read_person import *
from routes.update_person import *

@app.route("/")
def server():
    return "Stock management is working"

app.run(debug = True)