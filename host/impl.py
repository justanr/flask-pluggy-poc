from flask import Blueprint, render_template
from pluggy import HookimplMarker

hookimpl = HookimplMarker('fp')


bp = Blueprint('iunno', __name__)


@bp.route('/')
def bp_index():
    return 'hello'


@bp.route('/me')
def me():
    return 'hello me'


@bp.route('/template')
def template():
    return render_template("host.html")


@hookimpl
def fp_load_blueprints():
    return {'blueprint': bp, 'url_prefix': '/hello'}
