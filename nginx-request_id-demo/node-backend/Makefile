NAME=node-backend
TAG=node-backend

all: clean build run

build:
	docker build -t $(NAME) .

run:
	docker run -i -t -p 3001:3001 --name $(NAME) -d $(TAG)

clean:
	-docker stop $(NAME)
	-docker rm -f $(NAME)
