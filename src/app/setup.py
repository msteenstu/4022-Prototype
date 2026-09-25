'''
Author: Mckenna Steenbock
Description: The following code creates a set of test
users and an order to test the RBAC and cryptographic mechanisms.
'''

from app import db
from app.models import User, Order
import bcrypt

def create_users():
    if User.query.first() is not None:
        print(User.query.first())
        return

    db.session.add_all([
        User(
            email = "customer1@mail.com",
            password = bcrypt.hashpw(
                b'SuperSafePassword45!',
                bcrypt.gensalt()
            ),
            role = "customer"
        ),
        User(
            email = "admin33@mail.com",
            password = bcrypt.hashpw(
                b'AReallySecureP@ssword!',
                bcrypt.gensalt()
            ),
            role = "administrator"
        )
    ])
    db.session.commit()

def create_order():
    if Order.query.first():
        return
    
    customer = User.query.filter_by(email="customer1@mail.com").first()

    new_order = Order(
        shipping_address = "12345 Address Lane Denver Colorado",
        payment_card_number = 1234512345123451234,
        customer_id = customer.id
    )
    db.session.add(new_order)
    db.session.commit()