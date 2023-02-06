install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
format:
	# format stuff
lint:
	# lint stuff
test:
	# test stuff
deploy:
	# deploy stuff
all: install lint test deploy