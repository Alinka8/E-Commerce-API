from flask import Flask
from config import Config
from models import db
from schemas import ma
from routes.customer_routes import customer_bp
from routes.account_routes import account_bp
from routes.product_routes import product_bp
from routes.order_routes import order_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

app.register_blueprint(customer_bp, url_prefix='/api')
app.register_blueprint(account_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(order_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


