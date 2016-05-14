var express = require('express');
var winston = require('winston');

// Constants
var PORT = 3001;
var WLOG = "/var/log/node/express.log";
var date = new Date();

// Winston Setup
winston.add(winston.transports.File, { filename: WLOG });

// App
var app = express();
app.get('/', function (req, res) {
    res.send(req.headers);
    winston.log('info', req.headers);
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);
