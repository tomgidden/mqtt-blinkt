NAME=mqtt-blinkt
TAG=tomgidden/$(NAME)

build: Dockerfile $(NAME).py
	docker build . -t $(TAG)

push: build
	docker push $(TAG):latest

run: build
	docker run -d --rm -v $(PWD)/config.py:/app/config.py:ro $(TAG)

test: build
	docker run -it --rm -v $(PWD)/config.py:/app/config.py:ro $(TAG)
