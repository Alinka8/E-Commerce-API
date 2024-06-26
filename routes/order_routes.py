from flask import Blueprint, request, jsonify
from models import db, Order, OrderItem, Product
from schemas import order_schema, orders_schema, order_item_schema, order_items_schema

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['POST'])
def add_order():
    customer_id = request.json['customer_id']
    order_date = request.json['order_date']
    total_price = request.json['total_price']
    items = request.json.get('items', [])

    new_order = Order(customer_id=customer_id, order_date=order_date, total_price=total_price)
    db.session.add(new_order)
    db.session.commit()

    for item in items:
        product_id = item['product_id']
        quantity = item['quantity']
        new_order_item = OrderItem(order_id=new_order.id, product_id=product_id, quantity=quantity)
        db.session.add(new_order_item)
        db.session.commit()

    return order_schema.jsonify(new_order)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    all_orders = Order.query.all()
    return jsonify(orders_schema.dump(all_orders))

@order_bp.route('/orders/<id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)

@order_bp.route('/orders/<id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    order.customer_id = request.json['customer_id']
    order.order_date = request.json['order_date']
    order.total_price = request.json['total_price']
    db.session.commit()
    return order_schema.jsonify(order)

@order_bp.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return order_schema.jsonify(order)
