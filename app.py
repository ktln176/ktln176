from flask import Flask, render_template, request

from static.settings import Settings

app: Flask = Flask(__name__)


@app.route('/resume')
def resume():
    return render_template('html/resume.html')


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        print(request.args.get('a'))
        print(request.args.get('b'))
        print('This is a get request')
        return 'This is a get request'
    elif request.method == 'POST':
        json_data = request.form
        a = request.form.get('a')
        b = request.form.get('b')
        print(json_data)
        print(a)
        print(b)
        print('This is a post request')
        return 'This is a post request'
    return 'Hello World!'


if __name__ == '__main__':
    app.run(
        host=Settings.get_host(),
        debug=Settings.get_debug(),
        port=Settings.get_port()
    )
