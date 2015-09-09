"""pwf.response -- HTTP response representation."""

import collections


MULTIVALUED_HEADERS = {'Set-Cookie'}


class Response(object):
    """HTTP response."""

    def __init__(self, status, content_type='text/plain'):
        self.status = status
        self.headers = collections.OrderedDict()
        self.set_header('Content-type',  content_type)

    def set_header(self, name, value):
        """Set HTTP header."""
        if name in MULTIVALUED_HEADERS:
            self.headers.setdefault(name, []).append(value)
        else:
            self.headers[name] = value

    def get_headers_list(self):
        """Return headers as a list of tuples."""
        return self.headers.items()
