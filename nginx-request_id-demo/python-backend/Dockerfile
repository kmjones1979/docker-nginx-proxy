FROM centos:centos7
MAINTAINER Kevin Jones <kevin@nginx.com>

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all

ADD src /src

RUN cd /src; pip install -r requirements.txt

RUN mkdir -p /var/log/python

EXPOSE 8080

CMD ["python", "/src/index.py"]
