FROM centos:centos7
MAINTAINER "Kevin Jones - kevin@nginx.com"

WORKDIR /src/ruby/hello-world

# install dependencies
RUN yum install -y epel-release
RUN yum install -y gcc g++ make automake autoconf curl-devel openssl-devel nodejs
RUN yum install -y zlib-devel httpd-devel apr-devel apr-util-devel sqlite-devel


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

CMD ["bin/rails", "server", "-p", "4001", "-b", "0.0.0.0"]
