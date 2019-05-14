ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

run:
	flask run --host=0.0.0.0

reload:
	python db-restart.py

test:
	pytest ${ROOT_DIR}/tests -W ignore::DeprecationWarning

