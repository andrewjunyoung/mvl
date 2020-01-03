clean:
	find . | grep -E "(build|__pycache__|\.pyc|\.pyo)" | xargs rm -rf; rm -rf htmlcov; rm actual.*; rm .coverage

tree:
	tree -I 'docs|bin|lib|venv|htmlcov|.coverage'

tests:
	nosetests -v

coverage:
	nosetests -v --with-coverage
