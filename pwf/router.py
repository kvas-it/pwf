"""pwf.router -- routing support."""


class Router(object):
    """Router handles one level of routing."""

    def __init__(self):
        self.handler = None
        self.subrouters = {}

    def add_handler(self, path, handler):
        """Register handler for path.
        
        :param list path: parts of the path,
        :param handler: handler for the path.
        """
        if path:
            sub = self.subrouters.setdefault(path[0], Router())
            sub.add_handler(path[1:], handler)
        else:
            self.handler = handler

    def route(self, path):
        """Return handler and parameters extracted from the path.
        
        :param list path: parts of the path.
        :return: A tuple (handler, params) where handler is an object with
            methods corresponding to HTTP methods and params is a dictionary.
            If the route is not found, throws KeyError.
        """
        if path:
            sub = self.subrouters[path[0]]
            return sub.route(path[1:])
        else:
            return self.handler, {}
