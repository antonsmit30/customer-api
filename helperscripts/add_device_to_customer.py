import requests

def get_all():
    r = requests.get('http://13.58.251.121:8080/customers')
    print(r.text)


def get_customer(name):
    url = 'http://13.58.251.121:8080/customer/' + name
    r = requests.get(url)
    print(r.text)


def add_device(customer_name, device_name, device):
    """

    :param customer_name:
    :param device_name:
    :param device:
    :return text:
    """
    url = 'http://13.58.251.121:8080/customer/device/' + device_name
    data = {'customer_name': customer_name,
            'device': device}

    r = requests.post(url, data=data)
    print(r.text)



def main():

    # Running logic
    input_customer = input('Please specify customer name (lowercase): ')
    print('Customer info: ')
    get_customer(name=input_customer)

    while True:

        input_name = input('Please specify a device name: ')
        _device = input('Please specify ip: ')

        add_device(customer_name=input_customer, device_name=input_name, device=_device)

        user_input = input('Would you like to add another device ? \n1):  Y\n2)N')
        if user_input.upper() == 'N':
            break
        else:
            get_customer(name=input_customer)


if __name__ == '__main__':
    main()
