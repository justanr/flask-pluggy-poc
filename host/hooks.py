from pluggy import HookspecMarker


hookspec = HookspecMarker('fp')


@hookspec
def fp_load_blueprints():
    "Hook for loading blueprints"
    pass
