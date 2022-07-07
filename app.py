from flask import Flask

from static.blueprint.hello import hello_blue
from static.blueprint.resume import resume_blue
from static.settings import Settings

app: Flask = Flask(__name__)
app.config['DEBUG'] = Settings.get_debug()

# 蓝图
app.register_blueprint(hello_blue)
app.register_blueprint(resume_blue)


@app.route('/')
def ktln176():
    return "Hello!<br>This is ktln176's code notebook, only for learning and recording."


if __name__ == '__main__':
    app.run(
        host=Settings.get_host(),
        port=Settings.get_port()
    )
