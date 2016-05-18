import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import request

app = Flask(__name__)

log = '/var/log/python/python.log'

@app.route('/')
def index():
    print request.environ
    kv = request.headers
    for k, v in kv.iteritems():
        app.logger.info(request.method + ' ' + request.environ.get('PATH_INFO') +
                request.environ.get('QUERY_STRING') + ' ' +
                request.environ.get('SERVER_PROTOCOL') + " " +
                " ".join(map(lambda (k, v): '%s: "%s"' % (k, v), kv.iteritems())))
        return (request.method + ' ' + request.environ.get('PATH_INFO') +
                request.environ.get('QUERY_STRING') + ' ' +
                request.environ.get('SERVER_PROTOCOL') + " " +
                " ".join(map(lambda (k, v): '%s: "%s"' % (k, v), kv.iteritems())))

"""
kv = {}

for k, v in kv.iteritems():
  print "%s - %s" % (k, v)
  print "\n".join(map(lambda (k, v): "%s - %s" % (k, v), kv.iteritems())

"""

if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler(log, maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0')
