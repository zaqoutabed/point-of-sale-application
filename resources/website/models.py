from email.policy import default
from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    user_type = db.Column(db.Enum("staff", "admin"), default="staff")
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, default=datetime.now())
    sales = db.relationship('Sale', backref='user', lazy=True)
    purchases = db.relationship('Purchase', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(200), unique=True)
    stock = db.Column(db.Numeric(precision=10, scale=2), default=0)
    tax=db.Column(db.Integer, default=18)
    purchased_price = db.Column(db.Numeric(precision=10, scale=2), default=0)
    selling_price = db.Column(db.Numeric(precision=10, scale=2), default=0)
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, default=datetime.now())

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Numeric(precision=10, scale=2))
    subtotal_amount = db.Column(db.Numeric(precision=10, scale=2))
    eight_tax_amount = db.Column(db.Numeric(precision=10, scale=2))
    eighteen_tax_amount = db.Column(db.Numeric(precision=10, scale=2))
    customer_amount = db.Column(db.Numeric(precision=10, scale=2))
    change_amount = db.Column(db.Numeric(precision=10, scale=2))
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, default=datetime.now())
    sale_items = db.relationship('SaleItem', backref='sale', lazy=True)

class SaleItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    product_id = db.Column(db.Integer)
    product_barcode = db.Column(db.Integer)
    product_name = db.Column(db.String(200))
    product_tax=db.Column(db.Integer, default=18)
    product_purchased_price = db.Column(db.Numeric(precision=10, scale=2), default=0)
    product_selling_price = db.Column(db.Numeric(precision=10, scale=2), default=0)
    product_quantity = db.Column(db.Numeric(precision=10, scale=2))
    price_without_tax = db.Column(db.Numeric(precision=10, scale=2))
    tax_amount = db.Column(db.Numeric(precision=10, scale=2))
    total_amount = db.Column(db.Numeric(precision=10, scale=2))
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, default=datetime.now())

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    seller_name = db.Column(db.String(200))
    seller_invoice_number = db.Column(db.String(200))
    seller_fiscal_number = db.Column(db.Integer)
    seller_tax_number = db.Column(db.Integer)
    total_amount = db.Column(db.Numeric(precision=10, scale=2))
    subtotal_amount = db.Column(db.Numeric(precision=10, scale=2))
    eight_tax_amount = db.Column(db.Numeric(precision=10, scale=2))
    eighteen_tax_amount = db.Column(db.Numeric(precision=10, scale=2))
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, default=datetime.now())
    purchase_items = db.relationship('PurchaseItem', backref='purchase', lazy=True)

class PurchaseItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'), nullable=False)
    product_id = db.Column(db.Integer)
    product_barcode = db.Column(db.Integer)
    product_name = db.Column(db.String(200))
    product_tax=db.Column(db.Integer, default=18)
    product_purchased_price = db.Column(db.Numeric(precision=10, scale=2), default=0)
    product_selling_price = db.Column(db.Numeric(precision=10, scale=2), default=0)
    product_stock = db.Column(db.Numeric(precision=10, scale=2))
    price_without_tax = db.Column(db.Numeric(precision=10, scale=2))
    tax_amount = db.Column(db.Numeric(precision=10, scale=2))
    total_amount = db.Column(db.Numeric(precision=10, scale=2), default=0)
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, default=datetime.now())