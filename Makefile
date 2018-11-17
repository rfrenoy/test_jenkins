.PHONY: env unittests clean
.DEFAULT_GOAL := help

SHELL := /bin/bash
ENV_NAME := test_env
ENV_PY_VERSION = 3.6.*

env:
	conda create -n ${ENV_NAME} python=${ENV_PY_VERSION} -y && \
	conda install -y nose future coverage

unittests:
	source activate ${ENV_NAME} && \
	nosetests --cover-erase --with-coverage --cover-package=. --cover-html

clean:
	conda env remove -y -n ${ENV_NAME}