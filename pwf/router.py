"""pwf.router -- routing support."""


def match_path(pattern, path):
    """Match path with pattern and extract parameters if any.

    :param tuple pattern: pattern for matching the path,
    :param list path: parts of the path,
    :return: dictionary with extracted parameters or ``None`` if there was no
        match.
    """
    if len(pattern) != len(path):
        return None
    if len(path) == 0:
        return {}
    if pattern[0].startswith('$'):
        ret = match_path(pattern[1:], path[1:])
        if ret is None:
            return None
        else:
            param_name = pattern[0][1:]
            ret[param_name] = path[0]
            return ret
    if pattern[0] == path[0]:
        return match_path(pattern[1:], path[1:])


class Router(object):
    """Router handles one level of routing."""

    def __init__(self):
        self.map = {}

    def add_handler(self, path, handler):
        """Register handler for path.
        
        :param list path: parts of the path,
        :param handler: handler for the path.
        """
        path = tuple(path)
        # TODO: Think if allowing silent redefinition of paths is a good thing.
        # TODO: It would be also good to detect two paths that can match the
        #       same thing.
        self.map[path] = handler

    def route(self, path):
        """Return handler and parameters extracted from the path.
        
        :param list path: parts of the path.
        :return: a tuple (handler, params) where handler is an object with
            methods corresponding to HTTP methods and params is a dictionary.
            If the route is not found, throws KeyError.
        """
        # TODO: This will be slow for many URLs but we're unlikely to see that.
        for pattern, handler in self.map.items():
            params = match_path(pattern, path)
            if params is not None:
                return handler, params
        raise KeyError('Path not found')
