(function () {
    'use strict';
    angular
        .module('trace', [
            'trace.routes',
            'trace.authentication',
            'trace.config',
        ]);
    angular
        .module('trace.config',[]);
    angular
        .module('trace.routes', ['ngRoute']);

    angular
        .module('trace')
        .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();