from flask import Flask, render_template

from static.settings import Settings

app: Flask = Flask(__name__)


@app.route('/resume')
def start():
    return render_template('html/resume.html')


if __name__ == '__main__':
    app.run(
        host=Settings.get_host(),
        debug=Settings.get_debug(),
        port=Settings.get_port()
    )
