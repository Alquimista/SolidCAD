init:
	pip install pipenv
	pip install mkdocs
	pipenv install --dev

lock:
	pipenv lock

test:
	pipenv run python setup.py test

install:
	pip install .

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload