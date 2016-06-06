NAME=go-backend
TAG=go-backend

all: clean build run

build:
	docker build -t $(NAME) .

run:
	docker run -i -t -p 6001:6001 --name $(NAME) -d $(TAG)

clean:
	-docker stop $(NAME)
	-docker rm -f $(NAME)
