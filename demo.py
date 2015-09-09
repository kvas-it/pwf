"""Demo application for pwf web framework."""

import pwf

app = pwf.Application()

@app.path('/')
def index(request):
    return pwf.redirect(request, '/hello/')

@app.path('/hello/')
def hello(request, name=None):
    if name:
        return 'Hello {}!'.format(name)
    else:
        return 'Hello world!'

if __name__ == '__main__':
    app.demo_server()
