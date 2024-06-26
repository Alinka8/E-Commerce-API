from flask import Blueprint, request, jsonify
from models import db, Product
from schemas import product_schema, products_schema

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    stock = request.json['stock']
    new_product = Product(name=name, price=price, stock=stock)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

@product_bp.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return jsonify(products_schema.dump(all_products))

@product_bp.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

@product_bp.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    product.name = request.json['name']
    product.price = request.json['price']
    product.stock = request.json['stock']
    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

