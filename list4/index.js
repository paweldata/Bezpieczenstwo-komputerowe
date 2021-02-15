const bodyParser = require('body-parser');
const express = require('express');
const https = require('https');
const path = require('path');
const fs = require('fs');

var options = {
  key: fs.readFileSync("privkeyA.pem"),
  cert: fs.readFileSync("certA.crt"),
};

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.post("/stealData", function (req, res) {
  res.send(`I got your data! :D <br><br>
          user = ${req.body.username}<br>
          password = ${req.body.password}`);
});

https.createServer(options, app).listen(8443);
