(function () {
    'use strict';
    angular
        .module('trace.authentication', [
            'trace.authentication.controllers',
            'trace.authentication.services'
        ]);
    angular
        .module('trace.authentication.controllers', []);
    angular
        .module('trace.authentication.services', ['ngCookies']);
})();