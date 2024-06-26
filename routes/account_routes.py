from flask import Blueprint, request, jsonify
from models import db, CustomerAccount
from schemas import customer_account_schema, customer_accounts_schema

account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/customer_accounts', methods=['POST'])
def add_customer_account():
    customer_id = request.json['customer_id']
    username = request.json['username']
    password = request.json['password']
    new_account = CustomerAccount(customer_id=customer_id, username=username, password=password)
    db.session.add(new_account)
    db.session.commit()
    return customer_account_schema.jsonify(new_account)

@account_bp.route('/customer_accounts', methods=['GET'])
def get_customer_accounts():
    all_accounts = CustomerAccount.query.all()
    return jsonify(customer_accounts_schema.dump(all_accounts))

@account_bp.route('/customer_accounts/<id>', methods=['GET'])
def get_customer_account(id):
    account = CustomerAccount.query.get(id)
    return customer_account_schema.jsonify(account)

@account_bp.route('/customer_accounts/<id>', methods=['PUT'])
def update_customer_account(id):
    account = CustomerAccount.query.get(id)
    account.username = request.json['username']
    account.password = request.json['password']
    db.session.commit()
    return customer_account_schema.jsonify(account)

@account_bp.route('/customer_accounts/<id>', methods=['DELETE'])
def delete_customer_account(id):
    account = CustomerAccount.query.get(id)
    db.session.delete(account)
    db.session.commit()
    return customer_account_schema.jsonify(account)
