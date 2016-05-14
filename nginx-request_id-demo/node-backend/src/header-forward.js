var express = require('express');
var winston = require('winston');

// Constants
var PORT = 3001;
var WLOG = "/var/log/node/express.log";

// Winston Setup
winston.add(
  winston.transports.File, {
    filename: WLOG,
    level: 'info',
    json: true,
    eol: 'n', // for Windows, or `eol: ‘n’,` for *NIX OSs
    timestamp: true
  }
)

// App
var app = express();
app.get('/', function (req, res) {
    res.send(req.headers);
    winston.log(req.headers);
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);
