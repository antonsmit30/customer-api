from flask import Flask
from flask_restful import Api

from resources.customers import Customer, customerList


# App Configs
app=Flask(__name__)
api=Api(app)


# Here we will add out jwt using authenticate + identity

# Quick rest render
@app.route('/')
def home():
    return 'Message: API is callable', 201


# Resources here to add ie app.add_resource
api.add_resource(Customer, '/customer/<string:name>')
api.add_resource(customerList, '/customers')


# Init our app
if __name__ == '__main__':
    app.run(port=8080, debug=True)