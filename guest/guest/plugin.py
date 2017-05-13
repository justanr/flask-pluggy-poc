from flask import Blueprint
from pluggy import HookimplMarker

print("loaded plugin")

hookimpl = HookimplMarker('fp')
bp = Blueprint('guest', __name__)


@bp.route('/')
def index():
    return 'hello from guest'


@hookimpl
def fp_load_blueprints():
    print("from plugin")
    return bp, {'url_prefix': '/guest'}
