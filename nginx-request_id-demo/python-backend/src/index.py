from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    if 'x-request-id' in request.headers:
        reqi = request.headers.get('x-request-id')
        return 'X-Request-ID: ' + reqi
        for x in request.headers:
            return x
    else:
        return 'Please pass a X-Request-ID header'

if __name__ == '__main__':
    app.run()
