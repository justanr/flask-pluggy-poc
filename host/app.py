from . import hooks, impl
from flask import Flask
from pluggy import PluginManager


def create_app():
    pm = PluginManager('fp')
    pm.add_hookspecs(hooks)
    pm.register(impl)
    pm.load_setuptools_entrypoints('flaskplug')

    app = Flask(__name__)
    for bp in pm.hook.fp_load_blueprints():
        if isinstance(bp, dict):
            app.register_blueprint(**bp)
        elif isinstance(bp, tuple):
            app.register_blueprint(bp[0], **bp[1])
        else:
            app.register_blueprint(bp)

    return app
