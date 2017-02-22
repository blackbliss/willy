var app = angular.module('RadioApp', []);

app.controller('RadioController', function($scope, $http) {

  $scope.greetings = 'Cheers from Willy :)';

  $scope.getRadioStations = function()
  {
    // Simple GET request example:
    $http({
        method: 'GET',
        url: 'http://localhost:8080/api/stations'
    }).then(function successCallback(response) {
        // this callback will be called asynchronously
        // when the response is available
        $scope.greetings = response.data;
    }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        $scope.greetings = response;
    });

  };
});