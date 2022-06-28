env_activate = env/bin/activate

install:

	@test -d env || python3 -m venv env
	. $(env_activate) && python3 -m pip install -r requirements.txt

start:
	. $(env_activate) && python3 src/manage.py runserver


makemigrations:
	. $(env_activate) && python3 src/manage.py makemigrations

migrate:
	. $(env_activate) && python3 src/manage.py migrate

createsuperuser:
	. $(env_activate) && python3 src/manage.py createsuperuser

deploy:
	. $(env_activate) && python3 src/manage.py collectstatic

remove-env:
	rm -rf env
