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
    parser.add_argument('devices',
                        type=dict,
                        required=False)

    # Get Request
    def get(self, name):
        item = customerModel.find_by_name(name)
        if item:
            #return item.json()
            return item
        #Else return error
        return{'message': 'Item not found'}


    # Post Method - We will add more functionality later
    def post(self, name):

        # Add functionality to check if customer already exists

        # else
        data = Customer.parser.parse_args()

        item = customerModel(name, probe=data['probe'], devices=data['devices'])

        # Error handling
        try:
            print('item is: {}'.format(item))
            item.save_to_db()
        except:
            return{'Message': 'and error occured'}, 500
        else:
            return{'Message': 'item saved successfully'}


    # Delete method - WIP
    def delete(self, name):
        pass

    # Put method - WIP
    def put(self, name):
        pass


class customerList(Resource):

    # Get all customers - wip
    def get(self):
        pass
