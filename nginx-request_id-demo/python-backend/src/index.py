from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    if 'x-request-id' in request.headers:
        reqi = request.headers.get('x-request-id')
        return 'X-Request-ID: ' + reqi + '\n'
    else:
        return 'Please pass a X-Request-ID header\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
