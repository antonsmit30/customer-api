import sys
import requests

def run(url):
    r = requests.get(url)
    print(r.json())
    print([x for x in r.json()])


def main():
    """

    :return:
    """
    customer_name = sys.argv[1]
    url = 'http://13.58.251.121:8080/customer/' + customer_name

    run(url=url)


if __name__ == '__main__':
    main()
