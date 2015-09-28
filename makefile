.PHONY: devenv demo clean install uninstall test

DEVENV=__

PYTHON=${DEVENV}/bin/python
PIP=${DEVENV}/bin/pip
PYTEST=${DEVENV}/bin/py.test

devenv: ${DEVENV}

${DEVENV}:
	virtualenv ${DEVENV}
	${PYTHON} setup.py develop

${PYTEST}: ${DEVENV}
	${PIP} install pytest wsgi_intercept requests
	touch ${PYTEST}

test: ${PYTEST}
	${PYTEST} tests

demo:
	${PYTHON} demo.py

install:
	python setup.py install

uninstall:
	pip uninstall -y pwf

clean:
	rm -Rf ${DEVENV} .cache pwf.egg-info `find . -name *.pyc` build dist MANIFEST
