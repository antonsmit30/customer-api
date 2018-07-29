from flask import Flask
from flask_restful import Api


from resources.newdevices import DeviceResource
from resources.customers import Customer, customerList



# App Configs
app=Flask(__name__)
# DB configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api=Api(app)


# Here we will add out jwt using authenticate + identity

# Quick rest render
@app.route('/')
def home():
    return 'Message: API is callable', 201

# # Create all Tables
# # @app.before_first_request
# # def create_tables():
# #     db.create_all()


# Resources here to add ie app.add_resource
api.add_resource(DeviceResource, '/customer/device/<string:name>')
api.add_resource(Customer, '/customer/<string:name>')
api.add_resource(customerList, '/customers')



# Init our app
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=8080, debug=True)
