/**
 * Created by Gursimran on 20-Mar-16.
 */

angular
    .module('app')
    .controller('alarmCtrl', ['$scope', '$http', function($scope, $http) {
        // timer variables
        $scope.title = 'Alarm'
        $scope.mytime = new Date();
        $scope.hstep = 1;
        $scope.mstep = 15;
        $scope.ismeridian = true;

        // alarm status
        $scope.alarmStatus = 1;//getAlarmStatus();

        $http.get("/api/alarm").success(function(data) {
            $scope.alarms = data.objects;
        })

        $scope.addAlarm = function () {
            $http.post("/api/alarm", {
                "name":$scope.formData.name,
                "message":$scope.formData.message,
                "status":1,
                "severity":$scope.formData.severity,
                "days":$scope.formData.days,
                "time":$scope.formData.time,
                "deadline":$scope.formData.deadline,
            })
            .success(function (data) {
                    $scope.alarms.push(data);
            });

        }

        $scope.timeChanged = function() {
            //
        };

        $scope.updateAlarmStatus = function() {
            //
        }

        $scope.getAlarmStatus = function() {
            //
        }
    }])