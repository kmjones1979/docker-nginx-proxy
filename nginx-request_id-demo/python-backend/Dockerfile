FROM centos:centos7
MAINTAINER "Kevin Jones - kevin@nginx.com"

# set environment variables
ENV SPLUNK_FORWARDER_VERSION 6.2.2
ENV SPLUNK_FORWARDER_BUILD 255606
ENV SPLUNK_FORWARDER_CENTOS_URL https://download.splunk.com/products/splunk/releases/${SPLUNK_FORWARDER_VERSION}/universalforwarder/linux/splunkforwarder-${SPLUNK_FORWARDER_VERSION}-${SPLUNK_FORWARDER_BUILD}-linux-2.6-x86_64.rpm

# install dependencies
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip wget

# download and install splunk forwarder
RUN curl --show-error ${SPLUNK_FORWARDER_CENTOS_URL} -o splunkforwarder.rpm
RUN rpm -i splunkforwarder.rpm && rm splunkforwarder.rpm

# copy splunk configuration files
COPY opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf /opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf
COPY opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf /opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf

# install supervisord
RUN yum -y install python-setuptools
RUN easy_install supervisor
RUN mkdir -p /var/log/supervisor

# copy supervisord configuration file
COPY etc/supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# copy application source
ADD src /src

# install python requirements
RUN cd /src; pip install -r requirements.txt

# setup log folder
RUN mkdir -p /var/log/python

# clean up
RUN yum clean all

EXPOSE 5001 8089

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
