from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    print request.environ
    kv = request.headers
    for k, v in kv.iteritems():
        print (request.method + ' ' + request.environ.get('PATH_INFO') +
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
    app.run(host='0.0.0.0')
