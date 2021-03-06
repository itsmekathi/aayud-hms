(function () {
    'use strict';
    angular.module('app')
        .controller('contactsController', ['$scope', '$log', '$mdDialog', '$http', '$window',
            function ($scope, $log, $mdDialog, $http, $window) {
                $log.log('Contacts controller initialized');
                $scope.status = '  ';
                $scope.lookupName = '';
                $scope.customFullscreen = false;
                $scope.itemUrl = '/api/v1/contacts/'

                $scope.deleteMethod = 'DELETE';
                $scope.getMethod = 'GET';
                $scope.postMethod = 'POST';
                $scope.currentItemId = 0;

                // Angular material dialog
                $scope.showConfirm = function (ev, itemId) {
                    $scope.currentItemId = itemId;
                    var confirm = $mdDialog.confirm()
                        .title('Would you like to delete this item')
                        .textContent('This is an Irreversible action')
                        .targetEvent(ev)
                        .ok('Delete')
                        .cancel('Cancel');

                    $mdDialog.show(confirm).then(function () {
                        $log.log('Delete item action initialted');
                        deleteItem();
                    }, function () {
                        $log.log('Cancel action initialted');
                    });
                };

                var deleteItem = function () {
                    $http({
                        method: $scope.deleteMethod,
                        url: $scope.itemUrl + $scope.currentItemId
                    }).then(function (response) {
                        $scope.status = response.status;
                        $window.location.reload();
                    }, function (response) {
                        $scope.data = response.data.posts || 'Request failed';
                        $scope.status = response.status;
                    });
                };
            }]);
})();