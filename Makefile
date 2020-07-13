build:
	docker build -t flask-basic .

run:
	docker run -dp 5000:5000 -e MYSQL_TEST_HOST -e MYSQL_TEST_USER \
	-e MYSQL_TEST_PASSWORD -e MYSQL_TEST_DATABASE \
	-v ${PWD}:/lab-cicd flask-basic python hello.py

unit:
	docker run -v ${PWD}:/lab-cicd flask-basic pytest .