# Modules
# 1- Creating Modules
# 4- Packages
# from ecommerce.sales import calc_tax, calc_shipping (or)
from ecommerce.shopping import sales
from ecommerce.customer import contact

import sys

sales.calc_shipping()
sales.calc_tax()

# 2- compiled python file
# compiled file will get with .pyc extension
# sales.cpython-37.pyc

# 3- Module Search Path
print(sys.path)

# 5- Sub-packages
# create new package "shopping" and move "sales.py" into it.

# 7- The dir Function
print(dir(sales))
print(dir(contact))

print(sales.__name__)
print(sales.__package__)
print(sales.__file__)

# 8- Executing Modules as Script
