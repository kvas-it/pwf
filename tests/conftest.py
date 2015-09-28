# Configuration and common parts for the tests.

import pytest

from wsgiref.validate import validator
from wsgi_intercept import (requests_intercept,
        add_wsgi_intercept, remove_wsgi_intercept)

import pwf


def corrector(application):
    """Wrapper for wsgiref validator that corrects wsgi_intercept issues."""
    # Unfortunately wsgi_intercept messes up the types of some items in the
    # environ dict (at least according to wsgiref validator) so we need this
    # wrapper to correct them.
    def wrapped_app(environ, start_response):
        for key, value in environ.items():
            if isinstance(value, unicode) or isinstance(value, int):
                environ[key] = str(value)
        return application(environ, start_response)
    return wrapped_app


@pytest.fixture
def app(request):
    """Application that intercepts requests to http://test/."""
    app = pwf.Application()

    @app.path('/')
    def index(request):
        return 'index!'

    requests_intercept.install()
    add_wsgi_intercept('test', 80, lambda: corrector(validator(app)))

    def fin():
        remove_wsgi_intercept('test', 80)
        requests_intercept.uninstall()
    request.addfinalizer(fin)

    return app


