var app = angular.module('myApp', []);
app.controller('ledCtrl', function($scope) {
    //define init variable
    $scope.result = "LED is OFF ";
    $scope.lamp_state = "/static/lampOff.png";

    $scope.checkVal = function(val) {
        $scope.result = "LED is ";

        if (!val) {
            $scope.result += "OFF ";
            $scope.lamp_state = "/static/lampOff.png";
        } else {
            $scope.result += "ON ";
            $scope.lamp_state = "/static/lampOn.png";
        }
    };
}); //end of controller