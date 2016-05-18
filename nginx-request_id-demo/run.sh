docker run -i -t -p 5000:5000 --name python-backend -d python-backend
docker run -i -t -p 3001:3001 --name node-backend -d node-backend
docker run -i -t -p 7001:7001 --name go-backend -d go-backend
docker run -i -t -p 80:80 -p 6001:6001 --name nginx-frontend -d nginx-frontend
