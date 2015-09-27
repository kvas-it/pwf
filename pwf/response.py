"""pwf.response -- HTTP response representation."""

import collections


MULTIVALUED_HEADERS = {'Set-Cookie'}

# Very incomplete for now, but easy to extend.
HTTP_STATUS_MESSAGES = {
    200: 'OK',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See other',
    304: 'Not modified',
    307: 'Temporary Redirect',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not found',
    405: 'Method Not Allowed',
    500: 'Internal server error',
    501: 'Not Implemented'
}


class Response(object):
    """HTTP response."""

    def __init__(self, status=200, message=None, content_type='text/plain'):
        self.headers = collections.OrderedDict()
        self.set_status(status, message)
        self.set_header('Content-type',  content_type)

    def set_status(self, code, message=None):
        """Set HTTP status code and message.

        If the message is not provided it will be derived from the code.

        :param int code: status code.
        :param str message: status message (will be derived from the code if
            not provided or ``None``).
        """
        if code not in HTTP_STATUS_MESSAGES:
            raise ValueError('Status code {} is not supported'.format(code))
        if message is None:
            message = HTTP_STATUS_MESSAGES[code]
        self.status = '{} {}'.format(code, message)

    def set_header(self, name, value):
        """Set HTTP header."""
        if name in MULTIVALUED_HEADERS:
            self.headers.setdefault(name, []).append(value)
        else:
            self.headers[name] = value

    def get_headers_list(self):
        """Return headers as a list of tuples."""
        return self.headers.items()
