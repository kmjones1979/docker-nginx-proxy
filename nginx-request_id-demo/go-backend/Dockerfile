FROM centos:centos7
MAINTAINER "Kevin Jones - kevin@nginx.com"

# environment variables
ENV GO_VERSION 1.6.2
ENV GO_OS linux
ENV GO_ARCH amd64
ENV GO_URL https://storage.googleapis.com/golang/go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz
ENV PATH /usr/local/go/bin:$PATH
ENV tmp "/tmp/go/"

# copy go source and create go path structure
COPY src /usr/local/go/src
RUN mkdir -p /usr/local/go/bin
RUN mkdir -p /usr/local/go/pkg

# download and install go
RUN mkdir -p $tmp
RUN curl --show-error ${GO_URL} -o $tmp/go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz
RUN tar -C /usr/local -xzf $tmp/go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz

# cleanup
RUN rm -rf $tmp

EXPOSE 6001 8089

CMD ["go", "run", "/usr/local/go/src/hello-world/main.go"]
