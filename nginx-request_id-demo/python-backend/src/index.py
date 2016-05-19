import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import request

# application variables
app = Flask(__name__)

# logging variables
logp = '/var/log/python/python.log'
logf = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
logl = logging.INFO

@app.route('/')
def index():
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

if __name__ == '__main__':
    formatter = logging.Formatter(logf)
    handler = RotatingFileHandler(logp, maxBytes=10000, backupCount=1)
    handler.setLevel(logl)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logl)
    app.run(host='0.0.0.0', port=5001)
