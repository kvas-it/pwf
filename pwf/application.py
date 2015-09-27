"""pwf.application -- main application module."""

import types

from .error_handlers import HTTP404, HTTP405
from .path import is_error_path, split_path
from .request import Request
from .response import Response
from .router import Router


class Handler(object):
    """Handler proxy used for function handlers."""

    def __init__(self, method_map):
        self.__dict__ = method_map


class Application(object):
    """PWF web application"""

    def __init__(self):
        self.router = Router()
        self.router.add_handler(['#err_404'], HTTP404())
        self.router.add_handler(['#err_405'], HTTP405())

    def __call__(self, environ, start_response):
        """Entry point from WSGI."""
        response = Response()
        request = Request(environ, response)
        response_content = self.handle_request(request)
        # TODO: transform to iterable.
        start_response(response.status, response.get_headers_list())
        return response_content

    def handle_request(self, request):
        """Handle request."""
        try:
            handler, params = self.router.route(request.path)
        except KeyError:
            if is_error_path(request.path):
                # Fallback handler if everything fails.
                request.response.set_status(500)
                first_error = request.path[0][5:]
                return ['Error handler not found for {}.'.format(first_error)]
            else:
                request.path = ['#err_404']  # Not found.
                request.method = 'GET'
                return self.handle_request(request)

        try:
            handler_method = getattr(handler, request.method)
        except AttributeError:
            request.path = ['#err_405']  # Method not allowed.
            request.method = 'GET'
            return self.handle_request(request)

        request.add_params(params)
        return handler_method(request)

    def path(self, path, method='GET'):
        """Return a decorator for declaring a handler for the path."""
        path = split_path(path)
        def decorator(handler):
            if isinstance(handler, types.FunctionType):
                self.router.add_handler(path, Handler({method: handler}))
            elif isinstance(handler, types.ClassType):
                self.router.add_handler(path, handler())
            else:
                raise TypeError('Handler must be class or function')
            return handler

        return decorator

    def demo_server(self, host='localhost', port=5000):
        """Serve requests forever with wsgiref basic server."""
        # We import wsgiref only inside of this method because it's not needed
        # if we use a 'real' WSGI server.
        from wsgiref.simple_server import make_server
        server = make_server(host, port, self)
        print("Serving HTTP on {}:{}...".format(host, port))
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Interrupted.")
