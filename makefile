run:
	python manage.py run
clean:
	rm -rf *.pyc
shell:
	python manage.py shell
all: run clean
