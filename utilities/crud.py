from sqlalchemy.orm import Session
from utilities.models import User, Order
from datetime import date

# Users
def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, name: str, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.email = email
        db.commit()
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

# Orders
def create_order(db: Session, user_id: int, product_name: str, order_date: date):
    order = Order(user_id=user_id, product_name=product_name, order_date=order_date)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session):
    return db.query(Order).all()

def update_order(db: Session, order_id: int, product_name: str, order_date: date):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        order.product_name = product_name
        order.order_date = order_date
        db.commit()
    return order

def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
    return order
