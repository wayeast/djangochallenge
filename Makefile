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

clean:
	if [ -d ./env ] ; then \
		rm -rf env ; \
	fi
	find . -name *.pyc -delete

run: cheeseshop
	. $(VENV) && \
	$(PYTHON) -c "from a2r_app import app; app.run(debug=False)" && \
	deactivate

test: cheeseshop
	. $(VENV) && \
	$(PYTHON) tests/a2r_test.py && \
	deactivate
