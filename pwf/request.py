"""pwf.request -- HTTP request representation."""

from .path import split_path


class Request(object):
    """HTTP request."""

    def __init__(self, environ, response):
        self.environ = environ
        self.path = split_path(environ['PATH_INFO'])
        self.method = environ['REQUEST_METHOD']
        self.response = response
        self.params = {}

    def add_params(self, params):
        """Add parameters to request.
        
        :param dict params: Parameters.
        """
        for name, value in params.items():
            if name in self.params:
                existing = self.params[name]
                if isinstance(existing, list):
                    existing.append(value)
                else:
                    self.params = [existing, value]
            else:
                self.params[name] = value
