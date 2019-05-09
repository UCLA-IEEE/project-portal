ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

activate:
	. ${ROOT_DIR}/venv/bin/activate

reload: activate
	python db-restart.py

test: activate
	pytest ${ROOT_DIR}/tests -W ignore::DeprecationWarning

