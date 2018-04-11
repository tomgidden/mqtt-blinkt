NAME=mqtt-blinkt
TAG=tomgidden/rpi-$(NAME)

build: Dockerfile $(NAME).py
	docker build . -t $(TAG)

push: build
	docker push $(TAG):latest

run: build
	docker run -d --device /dev/gpiomem --rm -v $(PWD)/config.py:/app/config.py:ro --name $(NAME) $(TAG)

test: build
	docker run -it --device /dev/gpiomem --rm -v $(PWD)/config.py:/app/config.py:ro --name $(NAME) $(TAG)

stop:
	docker kill $(NAME)

clean:
	docker kill $(NAME); docker rmi $(TAG)
