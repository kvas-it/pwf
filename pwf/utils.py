"""pwf.utils -- utility functions and classes."""

from wsgiref.util import request_uri


def redirect(request, path, code=302, message=None):
    """Redirect client to another path in the application."""
    response = request.response
    response.set_status(code, message)
    env2 = dict(request.environ)
    t = path.split('?', 2)
    env2['PATH_INFO'] = t[0]
    if len(t) > 1:
        env2['QUERY_STRING'] = t[1]
    response.set_header('Location', request_uri(env2))
    return []
