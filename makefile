env_activate = env/bin/activate

install:
	@test -d env || python3 -m venv env
	. $(env_activate) && python3 -m pip install -r requirements.txt

start:
	. $(env_activate) && python3 src/manage.py runserver localhost:8000

makemigrations:
	. $(env_activate) && python3 src/manage.py makemigrations

migrate:
	. $(env_activate) && python3 src/manage.py migrate

createsuperuser:
	. $(env_activate) && python3 src/manage.py createsuperuser

staticfiles:
	. $(env_activate) && python3 src/manage.py collectstatic

dumpdata:
	. $(env_activate) && python3 src/manage.py dumpdata hittegods --indent 2 > src/hittegods/seeds/data_dump.json

loaddata:
	. $(env_activate) && python3 src/manage.py loaddata "src/hittegods/seeds/data_dump.json"

loadsampledata:
	. $(env_activate) && python3 src/manage.py loaddata "src/hittegods/seeds/sample_data.json"

make all: install makemigrations migrate staticfiles loaddata createsuperuser start

remove-env:
	rm -rf env
