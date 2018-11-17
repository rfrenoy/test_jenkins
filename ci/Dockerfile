FROM continuumio/miniconda3
ARG PYTHON_VERSION

COPY ./Makefile .
SHELL ["/bin/bash", "-c"]

RUN make env ENV_PY_VERSION=${PYTHON_VERSION}