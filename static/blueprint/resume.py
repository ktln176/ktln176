from flask import Blueprint, render_template

resume_blue = Blueprint('resume', __name__)


@resume_blue.route('/resume')
def resume():
    return render_template('html/resume.html')
