from flask import Flask, request

from utils import generate_emails
from utils import generate_names

import requests

app = Flask(__name__)


@app.route("/requirements/")
def open_file():
    return open("requirements.txt", "r")


@app.route("/generate-users/")
def generate_users():
    quantity_str = request.args.get('quantity', '100')

    if not quantity_str.isdigit():
        return 'Quantity should be a digit and >= 0'

    quantity = int(quantity_str)

    if quantity <= 0:
        return 'Quantity should be >= 0'

    if quantity > 999999:
        return 'Quantity should be less than 999999'

    names = generate_names(quantity)
    emails = generate_emails(quantity)
    result = ''

    for x in range(quantity):
        result = result + "'" + names[x] + ' ' + emails[x] + "'" + '<br>'
    return result


@app.route("/space/")
def space():
    response = requests.get('http://api.open-notify.org/astros.json')
    if response.status_code != 200:
        return 'Service Unavailable'

    astronaut_number = str(response.json()['number'])

    return astronaut_number


if __name__ == "__main__":
    app.run()
