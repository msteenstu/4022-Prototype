# ShopEasy Prototype

This repository contains a prototype of the e-commerce platform, ShopEasy. In this prototype, role-based authentication controls were implemented using a custom authorization wrapper (as seen in the `utils.py` file). At the database level, payment data was encrypted using the AES algorithm and a secret key stored in an environment variable file. This implementation can be examined in the `models.py` file. The `.env` file contains the flask secret key used to sign session cookies and the secret key used to encrypt payment data with AES. This file was only uploaded to GitHub for demonstration purposes and should not be used when the application is officially deployed.


## Set up the Prototype Test Environment

* Open a terminal window in the project repository
* Create a virtual environment: `python3 -m venv .venv`
* Activate the virtual environment: `source .venv/bin/activate`
* Install the requirements to run the application: `pip3 install -r requirements.txt`
* Configure the Flask application: `export FLASK_APP=src/app`
* Start the Flask application: `flask run`


### Verify Encryption Mechanism

* Open a terminal window in the project repository
* Access the sqlite3 database through the terminal: `sqlite3 instance/database.db`
* Type the following SQL command in the sqlite3 prompt: `SELECT * FROM Orders;`
* Review the contents of the Orders table and verify the payment card column contains enciphered text

### Test User Access Controls

* Login to the customer account using the following credentials:
  * Email: `customer1@mail.com`
  * Password: `SuperSafePassword45!`
* Observe that you are on the orders endpoint
* Try to access the following endpoint: `127.0.0.1:5000/admin`
* Observe the unauthorized error on the page
* Navigate back to the store orders page: `127.0.0.1:5000/orders`
* Logout of the customer account

### Test Administrator Access Controls

Note: For demonstration purposes, the administrative users can only access the admin dashboard and not the orders page.

* Login to the administrative account using the following credentials:
  * Email: `admin33@mail.com`
  * Password: `AReallySecureP@ssword!`
* Observe that you are on the admin endoint
* Try to access the following endpoint: `127.0.0.1:5000/orders`
* Observe the unauthorized error on the page
* Navigate back to the administrative dashboard: `127.0.0.1:5000/admin`
* Logout of the administrative account


### Note

* As of completing this prototype, SQLAlchemy had a major version update. This broke the SQLAlchemyUtils package and prevented the Flask application from running. An older version of SQLAlchemy was included in the `requirements.txt` file to allow the application to be tested.

References

ChuckMoe. (2022, September 12).  *How to use EncryptedType of SQLAlchemy [Online forum post]* . GitHub. **https://github.com/fastapi/sqlmodel/issues/447**

Kvesteri. (n.d.).  *sqlalchemy-utils/sqlalchemy_utils/types/encrypted/encrypted_type.py at master · kvesteri/sqlalchemy-utils* . GitHub. **https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/encrypted/encrypted_type.py#L227**

Steenbock, M. (2025). *CSC 3020 Final Project* (Version V1) [Software].

Hosted on GitHub

Steenbock, M. (2026). *CSC 3024 Final Project* (Version V1) [Software].

Hosted on GitHub
