PYTHON=./env/bin/python
PIP=./env/bin/pip
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
	fi

clean:
	if [ -d ./env ] ; then \
		rm -rf env ; \
	fi
	find . -name *.pyc -delete

run: cheeseshop
	. $(VENV) && \
	$(PYTHON) -c "from a2r_app import app; app.run(debug=False)"

test: cheeseshop
	. $(VENV) && \
	$(PYTHON) tests/a2r_test.py
