"""pwf.utils -- utility functions and classes."""

from urllib import quote


def reconstruct_url(environ):
    """Reconstruct requested URL from WSGI environment."""
    url = environ['wsgi.url_scheme']+'://'

    if environ.get('HTTP_HOST'):
        url += environ['HTTP_HOST']
    else:
        url += environ['SERVER_NAME']

        if environ['wsgi.url_scheme'] == 'https':
            if environ['SERVER_PORT'] != '443':
               url += ':' + environ['SERVER_PORT']
        else:
            if environ['SERVER_PORT'] != '80':
               url += ':' + environ['SERVER_PORT']

    url += quote(environ['SCRIPT_NAME'])
    url += quote(environ['PATH_INFO'])

    if environ.get('QUERY_STRING'):
        url += '?' + environ['QUERY_STRING']

    return url


def redirect(request, path, code=302, message=None):
    """Redirect client to another path in the application."""
    response = request.response
    response.set_status(code, message)
    env2 = dict(request.environ)
    t = path.split('?', 2)
    env2['PATH_INFO'] = t[0]
    if len(t) > 1:
        env2['QUERY_STRING'] = t[1]
    response.set_header('Location', reconstruct_url(env2))
    return []
