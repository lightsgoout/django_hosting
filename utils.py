def is_path_secure(path):
    """
    @type path unicode
    """
    if ".." in path:
        return False

    import re

    return re.match('^[a-zA-Z0-9_\.-/]+$', path) is not None


def is_valid_python_module(module):
    """
    @type module unicode
    """
    if ".." in module:
        return False

    if module.endswith('.'):
        return False

    import re

    return re.match('^[a-zA-Z0-9_\.]+$', module) is not None
