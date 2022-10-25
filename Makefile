install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py project1/*.py project2/*.py project3/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py project1/*.py project2/*.py

all: install format lint test