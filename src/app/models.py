'''
Author: Mckenna Steenbock
Description: The following code creates
database objects and relationships for the
user and order objects.
Note: Code to create the database objects was adapted from 
Steenbock (2026). The code used to encrypt payment data at the
column level was adapted from Kvesteri (n.d.), and ChuckMoe (2022).
'''

from flask_login import UserMixin
from app import db
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from dotenv import load_dotenv
import os

load_dotenv()

class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.LargeBinary, nullable = False)
    role = db.Column(db.String(20), nullable = False)

    orders = db.relationship(
        'Order',
        lazy = True,
        back_populates = 'customer'
    )

class Order(db.Model):
    __tablename__ = "Orders"
    id = db.Column(db.Integer, primary_key = True)
    shipping_address = db.Column(db.String(200), nullable = False)
    payment_card_number = db.Column(StringEncryptedType(
        db.String(25),
        os.getenv('AES_SECRET_KEY'),
        AesEngine,
        'pkcs5'
    ))

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('Users.id'),
        nullable = True
    )

    customer = db.relationship('User', back_populates='orders')