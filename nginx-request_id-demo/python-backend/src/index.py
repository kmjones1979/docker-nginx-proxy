from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    reqi = request.headers.get('x-request-id')
    return 'X-Request-ID: ' + reqi

if __name__ == '__main__':
    app.run()
