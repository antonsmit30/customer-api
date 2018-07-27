from db import db
from models.customers import customerModel


class DeviceModel(db.Model):

    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    device = db.Column(db.String(80))

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    customer = db.relationship('customerModel')

    def __init__(self, name, device, customer_id):
        # Our object
        self.name = name
        self.device = device
        self.customer_id = customer_id


    def json(self):
        return {'name': self.name, 'device': self.device}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def find_by_id(self, name):
        return DeviceModel.query.filter_by(name=name).first()

    def find_customer_id(self, name):
        return customerModel.find_by_name()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
