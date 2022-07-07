import json

from flask import Blueprint, request

hello_blue = Blueprint('hello', __name__)


@hello_blue.route('/hello', methods=['GET', 'POST'])
def hello():
    """hello"""
    if request.method == 'GET':
        return f'This is a get request!<br>' \
               f'request.args:{json.dumps(request.args)}'
    elif request.method == 'POST':
        return f'This is a post request!<br>' \
               f'request.args:{json.dumps(request.args)}<br>' \
               f'request.get_json():{json.dumps(request.get_json())}<br>' \
               f'request.form:{json.dumps(request.form)}'
    else:
        pass
