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
    app.demo_server()
