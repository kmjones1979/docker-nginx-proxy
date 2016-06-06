NAME=nginx-frontend
TAG=nginx-frontend

all: clean build run

build:
	docker build --build-arg API_KEY=$(API_KEY) -t $(NAME) .

run:
	docker run -i -t -p 80:80 -p 2001:2001 -p 7001:7001 --name $(NAME) -d $(TAG)

clean:
	-docker stop $(NAME)
	-docker rm -f $(NAME)
