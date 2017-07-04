"use strict";

var page = require('webpage').create();

setTimeout(function () {
    phantom.exit();
}, 5000);

page.open('http://localhost:5000/level5/login', 'post', 'username=admin&password=j6GM0bbCP8q9NQ1PotbZ1', function(status) {
    if (status !== 'success') {
        phantom.exit();
    } else {
        var session_id = null;
        for (var i in page.cookies) {
            if (page.cookies[i].name === 'session') {
                session_id = page.cookies[i].value;
            }
        }

        var redirectCount = 0;
        page.onUrlChanged = function(newUrl) {
            redirectCount += 1;
            if (redirectCount > 1) {
                page.stop();
            }
        }

        page.evaluate(function () {
            console.log('lol');
        });
    }
});

