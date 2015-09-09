# Demo for pwf web framework.

from __future__ import print_function

import pwf


app = pwf.Application()


@app.path('/')
def index(request, name=None):
    if name:
        return 'Hello {}!'.format(name)
    else:
        return 'Hello world!'


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 5000
    from wsgiref.simple_server import make_server
    server = make_server(HOST, PORT, app)
    print("Serving HTTP on {}:{}...".format(HOST, PORT))
    server.serve_forever()
