NAME=python-backend
TAG=python-backend

all: clean build run

build:
	docker build -t $(NAME) .

run:
	docker run -i -t -p 5001:5001 --name $(NAME) -d $(TAG)

clean:
	-docker stop $(NAME)
	-docker rm -f $(NAME)
