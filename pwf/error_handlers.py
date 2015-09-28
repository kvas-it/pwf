"""pwf.error_handlers -- Handlers for HTTP errors."""


class SimpleHandler(object):
    """A simple handler that just sets fixed status code and message."""

    status_code = 0
    message = ''

    def GET(self, request):
        request.response.set_status(self.status_code)
        return [self.message.format(**request.environ)]


class HTTP404(SimpleHandler):
    status_code = 404
    message = 'Path not found: {SCRIPT_NAME}{PATH_INFO}'


class HTTP405(SimpleHandler):
    status_code = 405
    message = ('Method {REQUEST_METHOD} is not allowed for path: '
               '{SCRIPT_NAME}{PATH_INFO}')


class HTTP500(SimpleHandler):
    status_code = 500
    message = 'The application crashed'
