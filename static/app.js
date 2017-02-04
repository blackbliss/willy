var app = angular.module('RadioApp', []);

app.controller('RadioController', function($scope, $http) {

  $scope.message = 'Cheers from Willy :)';

  this.getRadioStations = function()
  {
    // Simple GET request example:
    $http({
        method: 'GET',
        url: 'http://0.0.0.0:8080/api/stations'
    }).then(function successCallback(response) {
        // this callback will be called asynchronously
        // when the response is available
        $scope.message = response;
    }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        $scope.message = response;
    });

  };
});
