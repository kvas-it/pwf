.PHONY: devenv demo clean install uninstall test testcov htmlcov

DEVENV=__

PYTHON=${DEVENV}/bin/python
PIP=${DEVENV}/bin/pip
PYTEST=${DEVENV}/bin/py.test

devenv: ${DEVENV}

${DEVENV}:
	virtualenv ${DEVENV}
	${PYTHON} setup.py develop

${PYTEST}: ${DEVENV}
	${PIP} install pytest pytest-cov wsgi_intercept requests
	touch ${PYTEST}

test: ${PYTEST}
	${PYTEST} tests

testcov: ${PYTEST}
	${PYTEST} --cov=pwf tests

htmlcov: ${PYTEST}
	${PYTEST} --cov-report=html --cov=pwf tests

demo:
	${PYTHON} demo.py

install:
	python setup.py install

uninstall:
	pip uninstall -y pwf

clean:
	rm -Rf ${DEVENV} .coverage .cache htmlcov pwf.egg-info `find . -name *.pyc` build dist MANIFEST
