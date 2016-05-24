docker run -i -t -p 3001:3001 --name node-backend -d node-backend
docker run -i -t -p 4001:4001 --name ruby-backend -d ruby-backend
docker run -i -t -p 5001:5001 --name python-backend -d python-backend
docker run -i -t -p 6001:6001 --name go-backend -d go-backend
docker run -i -t -p 80:80 -p 2001:2001 -p 7001:7001 --name nginx-frontend -d nginx-frontend
