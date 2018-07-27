# Create our customer resource
# This class will be interfaced with the API frontend

from flask_restful import Resource, reqparse
from models.customers import customerModel

class Customer(Resource):

    # parser parameters
    parser = reqparse.RequestParser()
    parser.add_argument('probe',
                        type=int,
                        required=True,
                        help='Please specify probe port. If none specify 0'
                        )


    # Get Request
    def get(self, name):
        item = customerModel.find_by_name(name)
        if item:
            return item.json()
        #Else return error
        return{'message': 'Customer not found'}

    # Post Method - We will add more functionality later
    def post(self, name):

        # Add functionality to check if customer already exists
        if customerModel.find_by_name(name):
            return{'message': 'Customer with name {} already exists'.format(name)}, 400

        # else
        data = Customer.parser.parse_args()

        item = customerModel(name, probe=data['probe'])

        # Error handling
        try:
            print('item is: {}'.format(item))
            item.save_to_db()
        except:
            return{'Message': 'and error occurred'}, 500
        else:
            return{'Message': 'Customer saved successfully'}


    # Delete method - WIP
    def delete(self, name):
        pass

    # Put method - WIP
    def put(self, name):
        pass


class customerList(Resource):

    # Get all customers - wip
    def get(self):
        return {'items': list(map(lambda x: x.json(), customerModel.query.all()))}
