import sys
import requests

def main():
    """
    :param var1 - customer name
    :param var2 - device name
    :param var3 - device ip
    :return:
    """

    customer_name = sys.argv[1]
    device_name = sys.argv[2]
    device_ip = sys.argv[3]

    data = {'customer_name': customer_name,
            'device': device_ip}

    sv_device = device_name

    customer_name = sys.argv[1]
    device_name = sys.argv[2]
    device_ip = sys.argv[3]



    url = 'http://127.0.0.1:8080/customer/device/' + sv_device

    r = requests.post(url, data= data)

    print(r.text)

if __name__ == '__main__':
    main()
