# PWF

PWF is a WSGI web framework written as an exercise at writing plain WSGI
apps:

	import pwf
	
	app = pwf.Application()
	
	@app.path('/')
	def index(request):
        return 'Hello world!'
	
    app.demo_server()
    
To see it in action:

	make demo
