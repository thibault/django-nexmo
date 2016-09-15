test:
	flake8 djexmo --ignore=E501
	coverage run --branch --source=djexmo `which django-admin.py` test --settings=djexmo.test_settings djexmo
	coverage report --omit=djexmo/test*

.PHONY: test
