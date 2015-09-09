"""pwf.error_handlers -- Handlers for HTTP errors."""

class HTTP404(object):
    """Handler for HTTP 404."""

    def GET(self, request):
        request.response.status = '404 Not found'
        return ['Path not found: {}{}'.format(
            request.environ['SCRIPT_NAME'], request.environ['PATH_INFO'])]
