#!/bin/bash

echo -n "Enter your Amplify API key > "
read api_key

docker build --build-arg API_KEY="$api_key" -t nginx-frontend nginx-frontend/.
docker build -t python-backend python-backend/.
docker build -t node-backend node-backend/.
docker build -t go-backend go-backend/.
docker build -t ruby-backend ruby-backend/.
