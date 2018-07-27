# Create our Customer Model
# The customer Model will do the backend work (customer resource for front end requests)
from db import db


class customerModel(db.Model):


    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    probe = db.Column(db.Integer)

    # 1 customer to many Devices
    devices = db.relationship('DeviceModel', lazy='dynamic')


    #Init our customer
    def __init__(self, name, probe):
        self.name = name
        self.probe = probe


    def json(self):
        return {'name': self.name, 'probe': self.probe, 'devices': [devices.json() for devices in self.devices.all()]}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()



    def find_id_by_name(self, name):
        try:
            return customerModel.query.filter_by(name=name).first().id
        except AttributeError:
            return None


    # Save to DB
    # We will work on this later. for now just push to a list.
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Delete from DB
    # We will work on this later. for now just delete from list
    def delete_from_db(self, name):
        pass









