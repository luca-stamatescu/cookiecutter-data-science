.PHONY: all setup install_requirements download_data requirements docs

# Set name of virtual environment here
VENV = .venv
BIN = ${VENV}/bin/

all: setup docs tests

setup: ${VENV} install_requirements

${VENV}:
	python3 -m venv $@

install_requirements: requirements.txt
	$(BIN)pip install --upgrade pip
	$(BIN)pip install -r requirements.txt
	pre-commit install

download_data:

requirements:
	pip freeze > requirements.txt

submission:
	$(BIN)kaggle competitions submit -c titanic -f submissions/my_submission.csv -m "This submission was uploaded using make."

# Documentation
docs: docs/conf.py docs/index.rst
	sphinx-build -b html docs docs/_build

docker:
	-docker rm -f $(shell docker ps -aq)
	docker build --tag nameofdockerimage .
	docker run --name temporarycontainername nameofdockerimage

tests:
	pytest