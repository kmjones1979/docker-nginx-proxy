from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    if 'x-request-id' in request.headers:
        print request.headers
        print request.environ
        return (request.method + ' ' + request.environ.get('PATH_INFO') +
                ' ' + request.environ.get('SERVER_PROTOCOL') + '\n' +
                'User-Agent: ' + request.headers.get('user-agent') + '\n' +
                'Host: ' + request.headers.get('host') + '\n' +
                'Accept: ' + request.headers.get('accept') + '\n' +
                'X-Request-ID: ' + request.headers.get('x-request-id') + '\n')
    else:
        print request.headers
        print request.environ
        return (request.method + ' ' + request.environ.get('PATH_INFO') +
                ' ' + request.environ.get('SERVER_PROTOCOL') + '\n' +
                'User-Agent: ' + request.headers.get('user-agent')  + '\n' +
                'Host: ' + request.headers.get('host') + '\n' +
                'Accept: ' + request.headers.get('accept') + '\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
