GUNICORN=./env/bin/gunicorn
PIP=./env/bin/pip
PYTHON=./env/bin/python
VENV=./env/bin/activate


.PHONY: all \
	cheeseshop \
	clean \
	run \
	test

all: run

cheeseshop:
	if [ ! -d ./env ] ; then \
		virtualenv env ; \
		. $(VENV) ; \
		$(PIP) install -r requirements.txt ; \
		deactivate ; \
	fi
	if [ ! -d ./log ] ; then \
		mkdir log ; \
	fi

clean:
	if [ -d ./env ] ; then \
		rm -rf env ; \
	fi
	rm -rf log
	find . -name *.pyc -delete

run: cheeseshop
	. $(VENV) && \
	echo Starting server... && \
	$(GUNICORN) -c gunicorn.py a2r_app:app && \
	deactivate

test: cheeseshop
	. $(VENV) && \
	$(PYTHON) tests/a2r_test.py && \
	deactivate
