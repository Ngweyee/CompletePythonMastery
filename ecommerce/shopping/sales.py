from ecommerce.customer import contact
from ..customer import contact

# 6- Intra-package References
# . mean one level in package structure ecommerce,
# .. means customer and shopping package level

contact.contact_customer()

# print("Sales initializes", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("Sales started")
    calc_tax()
