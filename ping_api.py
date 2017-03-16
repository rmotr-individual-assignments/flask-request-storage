import argparse
import requests


def make_request(method, url):
    return requests.request(method.lower(), url)


def main():
    parser = argparse.ArgumentParser(
        description='Ping the API to insert test data.')
    parser.add_argument(
        "method",
        help="HTTP Method used for the testing request",
        choices=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
    parser.add_argument("-u", "--url", help="URL of the API",
                        default='http://localhost:8080/home')

    args = parser.parse_args()
    resp = make_request(args.method, args.url)
    if resp.ok:
        print("Response successful: {}".format(resp.status_code))
    else:
        print("An error occurred with the request: {}".format(
            resp.status_code))


if __name__ == '__main__':
    main()
