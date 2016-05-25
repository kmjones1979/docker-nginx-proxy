FROM centos:centos7

MAINTAINER "Kevin Jones - kevin@nginx.com"

# set environment variables
ENV SPLUNK_FORWARDER_VERSION 6.2.2
ENV SPLUNK_FORWARDER_BUILD 255606
ENV SPLUNK_FORWARDER_CENTOS_URL https://download.splunk.com/products/splunk/releases/${SPLUNK_FORWARDER_VERSION}/universalforwarder/linux/splunkforwarder-${SPLUNK_FORWARDER_VERSION}-${SPLUNK_FORWARDER_BUILD}-linux-2.6-x86_64.rpm

# environment
ARG API_KEY

# install NGINX amplify agent
RUN mkdir -p /tmp/amplify/
RUN curl -L -o /tmp/amplify/amplify-install.sh \
               https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh
RUN sh ./tmp/amplify/amplify-install.sh -y || echo "continue..."

# install dependencies
RUN yum install -y wget gcc gcc-c++ make zlib-devel pcre-devel openssl-devel mercurial epel-release
RUN yum update -y

# install splunkforwarder
RUN curl --show-error ${SPLUNK_FORWARDER_CENTOS_URL} -o splunkforwarder.rpm
RUN rpm -i splunkforwarder.rpm && rm splunkforwarder.rpm

# copy splunk configuration
COPY opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf /opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf
COPY opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf /opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf

# install supervisord
RUN yum -y install python-setuptools
RUN easy_install supervisor
RUN mkdir -p /var/log/supervisor

# copy supervisor configuration
COPY etc/supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# download nginx source code
RUN hg clone http://hg.nginx.org/nginx /tmp/nginx/src

# build nginx from source
RUN cd /tmp/nginx/src && ./auto/configure \
    --prefix=/etc/nginx/ \
    --sbin-path=/usr/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --user=nginx \
    --group=nginx \
    --with-http_v2_module \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_sub_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_stub_status_module \
    --with-http_auth_request_module \
    --with-mail \
    --with-mail_ssl_module \
    --with-file-aio \
    --with-ipv6
RUN cd /tmp/nginx/src && make && make install

# copy static Nginx Plus files
COPY etc/nginx /etc/nginx

# clean up
RUN rm -rf /tmp/*

# clean up
RUN yum clean all

EXPOSE 80 443 7001 8080 8089

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
