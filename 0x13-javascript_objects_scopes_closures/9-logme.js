#!/usr/bin/node
let ccount = 0;
exports.logMe = function (item) { console.log(`${ccount++}: ${item}`); };
