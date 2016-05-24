FROM centos:centos7
MAINTAINER "Kevin Jones - kevin@nginx.com"

WORKDIR /src/ruby/hello-world

# set environment variables
ENV SPLUNK_FORWARDER_VERSION 6.2.2
ENV SPLUNK_FORWARDER_BUILD 255606
ENV SPLUNK_FORWARDER_CENTOS_URL https://download.splunk.com/products/splunk/releases/${SPLUNK_FORWARDER_VERSION}/universalforwarder/linux/splunkforwarder-${SPLUNK_FORWARDER_VERSION}-${SPLUNK_FORWARDER_BUILD}-linux-2.6-x86_64.rpm

# install dependencies
RUN yum install -y epel-release
RUN yum update -y
RUN yum install -y gcc g++ make automake autoconf curl-devel openssl-devel nodejs
RUN yum install -y zlib-devel httpd-devel apr-devel apr-util-devel sqlite-devel

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

# install ruby, gems qnd rails
RUN yum install -y ruby-rdoc ruby-devel
RUN yum install -y rubygems
RUN gem update
RUN gem install bundler --no-ri --no-rdoc

# deploy application
RUN mkdir -p /src/ruby/
RUN mkdir -p /var/log/ruby/
COPY src/ruby/hello-world /src/ruby/hello-world
RUN bin/bundle install --path vendor/cache

# clean up
RUN yum clean all

EXPOSE 4001 8089

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
