def is_path_secure(path):
    if ".." in path:
        return False

    import re

    return re.match('^[a-zA-Z0-9_\.-/]+$', path) is not None
