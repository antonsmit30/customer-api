from flask_restful import Resource, reqparse
from models.newdevices import DeviceModel
from models.customers import customerModel


class DeviceResource(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('customer_name',
                        type=str,
                        required=True,
                        help='Please specify Customer name to link.'
                        )

    parser.add_argument('device',
                        type=str,
                        required=True,
                        help='Please specify device name'
                        )


    # Get Request
    def get(self, name):

        data = DeviceResource.parser.parse_args()

        item = DeviceModel.find_by_name(name)
        if item:
            return item.json()
        #Else return error
        return{'message': 'Item not found'}

    # Post Method - We will add more functionality later
    def post(self, name):

        # Add functionality to check if customer already has device
        # if DeviceModel.find_by_name(name):
        #     return{'message': 'Customer with name {} already exists'.format(name)}, 400

        # else
        data = DeviceResource.parser.parse_args()

        customer_id = DeviceModel.find_id_by_name(name=data['customer_name'])

        # Customer not exist
        if customer_id == None:
            return{'Message': 'Customer does not exist. Create first'}, 404


        item = DeviceModel(name, data['device'], customer_id=customer_id)

        # Error handling
        try:
            print('item is: {}'.format(item))
            item.save_to_db()
        except:
            return{'Message': 'and error occured'}, 500
        else:
            return{'Message': 'item saved successfully'}