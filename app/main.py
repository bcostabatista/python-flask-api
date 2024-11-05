from flask import Flask, jsonify
import requests
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_BASE_URL = os.getenv('API_BASE_URL')

"""
decorators can be used to process
something before or after the functions
it's decorating is called, it receives
a function as an argument.

the function it receives as an argument
is the function it's decorating.
"""


def route_decorator(func):
    """
    wrapper functions in decorators are
    usually needed but not required.

    You can use both *args and **kwargs in
    the same function definition. When doing so,
    *args must come before **kwargs

    *args: allows a function to accept any
    number of positional arguments.

    **kwargs: allows a function to accept any
    number of keyword arguments.
    """
    def wrapper(*args, **kwargs):
        logger.info("decorating with decorators")
        return func(*args, **kwargs)
    return wrapper


@app.route('/api/v1/resource', methods=['GET'])
@route_decorator
def get_resource():
    data = requests.get(f"{API_BASE_URL}/projects").json()

    projects = {}
    for d in data:
        if d["namespace"]["id"] not in projects:
            projects[d["namespace"]["id"]] = []

        projects[d["namespace"]["id"]].append(d["name"])

    return jsonify(projects), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
