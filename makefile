.PHONY: devenv clean install uninstall

devenv: __

__:
	virtualenv __
	__/bin/python setup.py develop

install:
	python setup.py install

uninstall:
	pip uninstall -y pwf

clean:
	rm -Rf __ pwf.egg-info `find . -name *.pyc` build dist MANIFEST
