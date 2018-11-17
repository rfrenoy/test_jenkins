FROM continuumio/miniconda3
ARG PYTHON_VERSION

COPY ./Makefile .
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y make
RUN make env ENV_PY_VERSION=${PYTHON_VERSION}