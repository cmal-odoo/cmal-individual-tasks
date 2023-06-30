odoo.define('kinsman.main', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var domReady = require('web.dom_ready');

    domReady.then(function() {
        $('#toggle_hide_prices').click(function() {
            ajax.jsonRpc('/toggle_hide_prices', 'call', {})
                .then(function (data) {
                    location.reload();
                });
        });
    });
});
