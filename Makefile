test:
	flake8 nexmo --ignore=E501
	coverage run --branch --source=nexmo `which django-admin.py` test --settings=nexmo.test_settings nexmo
	coverage report --omit=nexmo/test*

.PHONY: test
