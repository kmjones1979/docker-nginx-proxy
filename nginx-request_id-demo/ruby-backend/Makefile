NAME=ruby-backend
TAG=ruby-backend

all: clean build run

build:
	docker build -t $(NAME) .

run:
	docker run -i -t -p 4001:4001 --name $(NAME) -d $(TAG)

clean:
	-docker stop $(NAME)
	-docker rm -f $(NAME)
