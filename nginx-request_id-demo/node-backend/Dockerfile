FROM centos:centos7

# install dependencies
RUN yum install -y epel-release
RUN yum install -y nodejs npm

# copy node app configuration
COPY src/package.json /src/package.json

# install node
RUN cd /src; npm install --production

# copy application source folder
COPY src /src

EXPOSE  3001

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
