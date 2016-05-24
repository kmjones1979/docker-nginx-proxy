FROM centos:centos7
MAINTAINER "Kevin Jones - kevin@nginx.com"

# environment variables
ENV GO_VERSION 1.6.2
ENV GO_OS linux
ENV GO_ARCH amd64
ENV GO_URL https://storage.googleapis.com/golang/go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz
ENV PATH /usr/local/go/bin:$PATH
ENV SPLUNK_FORWARDER_VERSION 6.2.2
ENV SPLUNK_FORWARDER_BUILD 255606
ENV SPLUNK_FORWARDER_CENTOS_URL https://download.splunk.com/products/splunk/releases/${SPLUNK_FORWARDER_VERSION}/universalforwarder/linux/splunkforwarder-${SPLUNK_FORWARDER_VERSION}-${SPLUNK_FORWARDER_BUILD}-linux-2.6-x86_64.rpm
ENV tmp "/tmp/"

# NGINX amplify API key setup
ARG API_KEY
RUN mkdir -p /etc/amplify-agent/
COPY etc/amplify-agent/agent.conf /etc/amplify-agent/agent.conf

# install dependencies
RUN yum install -y epel-release wget initscripts iproute iptables libmnl \
        libnetfilter_conntrack libnfnetlink sysvinit-tools
RUN yum update -y

# amplify repo setup
COPY etc/yum.repos.d/nginx-amplify.repo /etc/yum.repos.d/nginx-amplify.repo
RUN curl -L http://nginx.org/keys/nginx_signing.key -o $tmp/nginx_signing.key
RUN rpmkeys --import $tmp/nginx_signing.key

# NGINX amplify install
RUN yum install -y nginx-amplify-agent

#log setup
RUN mkdir -p /var/log/amplify-agent/
RUN touch /var/log/amplify-agent/agent.log

#RUN ln -sf /dev/stdout /var/log/amplify-agent/agent.log

# install NGINX amplify agent
RUN curl -L -o amplify-install.sh \
               https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh && \
               sh ./amplify-install.sh && \
               rm -f ./amplify-install.sh

# install splunkforwarder
RUN curl --show-error ${SPLUNK_FORWARDER_CENTOS_URL} -o splunkforwarder.rpm
RUN rpm -i splunkforwarder.rpm && rm splunkforwarder.rpm

# install supervisord
RUN yum -y install python-setuptools
RUN easy_install supervisor
RUN mkdir -p /var/log/supervisor

# copy splunk configuration files
COPY opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf /opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf
COPY opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf /opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf

# copy supervisor configuration
COPY etc/supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# copy go source and create go path structure
COPY src /usr/local/go/src
RUN mkdir -p /usr/local/go/bin
RUN mkdir -p /usr/local/go/pkg
RUN mkdir -p /var/log/go/

# download and install go
RUN mkdir -p $tmp
RUN curl --show-error ${GO_URL} -o $tmp/go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz
RUN tar -C /usr/local -xzf $tmp/go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz

# cleanup
RUN rm -rf $tmp/*
RUN yum clean all

EXPOSE 6001 8089

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
