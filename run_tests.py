from general.config import *
from models.product import *
from tests import product_tests, permission_tests, person_tests

product_tests.run()
permission_tests.run()
person_tests.run()