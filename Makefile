DEBUG_SET=--settings=arabic2roman.settings.debug
DJ_PY=python manage.py
GUNICORN=gunicorn
PIP=pip
BASE_SET=--settings=arabic2roman.settings.base
VENV=. env/bin/activate


.PHONY: all \
	cheeseshop \
	clean \
	run \
	run_debug \
	test

all: run

cheeseshop:
	if [ ! -d ./env ] ; then \
		virtualenv env ; \
		$(VENV) ; \
		$(PIP) install -r requirements.txt ; \
		deactivate ; \
	fi
	if [ ! -d ./log ] ; then \
		mkdir log ; \
	fi
	$(VENV) && \
	$(DJ_PY) migrate $(BASE_SET) && \
	deactivate

clean:
	if [ -d ./env ] ; then \
		rm -rf env ; \
	fi
	if [ -f db.sqlite3 ] ; then \
		rm db.sqlite3 ; \
	fi
	if [ -d ./log ] ; then \
		rm -rf log ; \
	fi
	find . -name *.pyc -delete

run: cheeseshop
	$(VENV) && \
	echo Starting server... && \
	$(GUNICORN) -c gunicorn_conf.py arabic2roman.wsgi && \
	deactivate

run_debug: cheeseshop
	$(VENV) && \
	echo Starting debug server... && \
	$(DJ_PY) runserver $(DEBUG_SET) && \
	deactivate

test: cheeseshop
	$(VENV) && \
	$(DJ_PY) test $(BASE_SET) && \
	deactivate
