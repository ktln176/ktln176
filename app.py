import logging

from flask import Flask, request

from static.blueprint.resume import resume_blue
from static.logger import Logger
from static.settings import Settings

app: Flask = Flask(__name__)
app.register_blueprint(resume_blue)


@app.route('/hello', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        print(request.args.get('a'))
        print(request.args.get('b'))
        print('This is a get request!')
        return 'This is a get request!'
    elif request.method == 'POST':
        json_data = request.form
        a = request.form.get('a')
        b = request.form.get('b')
        print(json_data)
        print(a)
        print(b)
        print('This is a post request!')
        return 'This is a post request!'
    return "Hello World!   This is ktln176's notebook."


if __name__ == '__main__':
    Logger.init_logger()
    logging.info('ktln176 web server now start!')
    app.run(
        host=Settings.get_host(),
        debug=Settings.get_debug(),
        port=Settings.get_port()
    )
