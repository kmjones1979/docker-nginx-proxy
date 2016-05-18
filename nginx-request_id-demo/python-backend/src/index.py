from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    if 'x-request-id' in request.headers:
        print request.headers
        return ('User-Agent:\t ' + request.headers.get('user-agent') + '\n' +
                'Host:\t\t ' + request.headers.get('host') + '\n' +
                'Accept:\t\t ' + request.headers.get('accept') + '\n' +
                'X-Request-ID:\t ' + request.headers.get('x-request-id') + '\n')
    else:
        print request.headers
        return ('User-Agent:\t ' + request.headers.get('user-agent')  + '\n' +
                'Host:\t\t ' + request.headers.get('host') + '\n' +
                'Accept:\t\t ' + request.headers.get('accept') + '\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
