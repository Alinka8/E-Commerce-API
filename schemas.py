from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Customer, CustomerAccount, Product, Order, OrderItem

ma = Marshmallow()

class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class CustomerAccountSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerAccount

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order

class OrderItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
customer_account_schema = CustomerAccountSchema()
customer_accounts_schema = CustomerAccountSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)
