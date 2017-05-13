from flask import Blueprint, render_template
from pluggy import HookimplMarker

print("loaded plugin")

hookimpl = HookimplMarker('fp')
bp = Blueprint('guest', __name__, template_folder="templates",
               static_folder="static")


@bp.route('/')
def index():
    return 'hello from guest'


@bp.route('/template')
def template():
    return render_template("hello.html")


@hookimpl
def fp_load_blueprints():
    print("from plugin")
    return bp, {'url_prefix': '/guest'}
