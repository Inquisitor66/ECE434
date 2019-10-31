#!/usr/bin/env node
//Slider controls an LED connect to P9_14
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');


const LED = 'P9_14';
const AUTH = 'Qv7g4ylooHAmJe2xE67cmW6mGpVuDBxd';
b.pinMode(LED, b.OUTPUT);

var blynk = new Blynk.Blynk(AUTH);
var v1 = new blynk.VirtualPin(1);


v1.on('write', function(param) {
	console.log('V1:', param[0]);
	b.analogWrite(LED, param[0]);
});



