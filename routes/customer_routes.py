from flask import Blueprint, request, jsonify
from models import db, Customer
from schemas import customer_schema, customers_schema

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/customers', methods=['POST'])
def add_customer():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    new_customer = Customer(name=name, email=email, phone=phone)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.jsonify(new_customer)

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    all_customers = Customer.query.all()
    return jsonify(customers_schema.dump(all_customers))

@customer_bp.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    return customer_schema.jsonify(customer)

@customer_bp.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)
    customer.name = request.json['name']
    customer.email = request.json['email']
    customer.phone = request.json['phone']
    db.session.commit()
    return customer_schema.jsonify(customer)

@customer_bp.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return customer_schema.jsonify(customer)
