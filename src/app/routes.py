'''
Author: Mckenna Steenbock
Description: The following python file
defines the endpoints of the prototype
web application.
'''
from flask import redirect, render_template, url_for
from flask_login import current_user, login_user, login_required, logout_user
from app import app, db
from flask_wtf import FlaskForm
from app.models import User, Order
from app.utils import role_required
from app.forms import LoginForm
import bcrypt

@app.route('/index')
@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        auth_user = User.query.filter_by(email=form.email.data).first()
        if auth_user and bcrypt.checkpw(
            form.password.data.encode('utf-8'),
            auth_user.password
        ):
            login_user(auth_user)

            if auth_user.role == "administrator":
                return redirect(url_for('admin_dashboard'))

            return redirect(url_for('customer_dashboard'))
    return render_template('login.html', form = form)

@app.route('/admin')
@login_required
@role_required('administrator')
def admin_dashboard():
    return render_template('admin.html')

@app.route('/orders')
@login_required
@role_required('customer')
def customer_dashboard():
    orders = current_user.orders
    
    return render_template('customer.html', orders = orders)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')