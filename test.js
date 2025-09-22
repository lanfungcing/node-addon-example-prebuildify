'use strict'

var binding= require('node-gyp-build')(__dirname);

require('assert').equal(binding.hello(),"hello");
