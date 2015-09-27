"""pwf.error_handlers -- Handlers for HTTP errors."""


class HTTP404(object):
    """Handler for HTTP 404."""

    def GET(self, request):
        request.response.set_status(404)
        return ['Path not found: {}{}'.format(
            request.environ['SCRIPT_NAME'], request.environ['PATH_INFO'])]


class HTTP405(object):
    """Handler for HTTP 405."""

    def GET(self, request):
        request.response.set_status(405)
        return ['Method {} is not allowed for path: {}{}'.format(
            request.environ['REQUEST_METHOD'],
            request.environ['SCRIPT_NAME'], request.environ['PATH_INFO'])]
