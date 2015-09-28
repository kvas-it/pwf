# Tests for pwf.application.

import pytest
import requests


@pytest.mark.usefixtures('app')
def test_root():
    r = requests.get('http://test/')
    assert r.status_code == 200
    assert r.text == 'index!'


@pytest.mark.usefixtures('app')
def test_404():
    r = requests.get('http://test/not_there')
    assert r.status_code == 404
    assert r.text == 'Path not found: /not_there'


def test_405(app):
    @app.path('/hello')
    def hello(request):
        return 'ok'

    r = requests.post('http://test/hello')
    assert r.status_code == 405
    assert r.text == 'Method POST is not allowed for path: /hello'


def test_500(app):
    @app.path('/explode')
    def explode(request):
        return 1/0

    r = requests.get('http://test/explode')
    assert r.status_code == 500
    assert r.text == 'The application crashed'


def test_arg(app):
    @app.path('/hello/$name')
    def hello(request, name):
        return 'Hello, {}!'.format(name)

    r = requests.get('http://test/hello/nurse')
    assert r.text == 'Hello, nurse!'


def test_class_handler(app):
    @app.path('/counter')
    class Handler(object):
        def __init__(self):
            self.counter = 0
        def GET(self, request):
            self.counter += 1
            return str(self.counter)

    r = requests.get('http://test/counter')
    assert r.text == '1'
    r = requests.get('http://test/counter')
    assert r.text == '2'


def test_bad_handler(app):
    with pytest.raises(TypeError):
        app.path('/hello')('bad handler')
