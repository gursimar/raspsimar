/**
 * Created by Gursimran on 20-Mar-16.
 */

angular
    .module('app')
    .controller('alarmCtrl', ['$scope', '$uibModal', '$http', function($scope, $uibModal, $http) {
        // timer variables
        $scope.title = 'Alarm'

        $http.get("/api/alarm").success(function(data) {
            $scope.alarms = data.objects;
        })

        $scope.timeChanged = function() {
            //
        };

        $scope.updateAlarm = function (alarm) {
            if (alarm.id == null) {
                //alert('Adding alarm')
                $http.post("/api/alarm", {
                        "name": alarm.name,
                        "message": alarm.message,
                        "status": alarm.status, // by default status of alarm is on
                        "severity": alarm.severity,
                        "days": alarm.days,
                        "time": alarm.time,
                        "deadline": alarm.deadline,
                })
                .success(function (data) {
                    $scope.alarms.push(data);
                    //alert ('Alarm added');
                });
            }
            else {
                //alert('Updating alarm')
                $http.put("/api/alarm/" + alarm.id, {
                        "name": alarm.name,
                        "message": alarm.message,
                        "status": alarm.status,
                        "severity": alarm.severity,
                        "days": alarm.days,
                        "time": alarm.time,
                        "deadline": alarm.deadline,
                })
                .success(function (data) {
                    //alert('updating alarm')
                    //$scope.updateData($scope.alarms, alarm)
                    //$scope.alarms.push(data);
                });
            }
        }

        $scope.updateData = function (alarms, pAlarm) {
            for (alarm in alarms) {
                if (pAlarm.id == alarm.id) {
                    // the particular alarm is found
                        alarm.name = pAlarm.name;
                        alarm.message = pAlarm.message;
                        alarm.status = pAlarm.status;
                        alarm.severity = pAlarm.severity
                        alarm.days = pAlarm.days
                        alarm.time = pAlarm.time
                        alarm.deadline = pAlarm.deadline
                }
            }
        };

        $scope.animationsEnabled = true;

        $scope.createModal = function (alarm) {
            var modalInstance = $uibModal.open({
              animation: $scope.animationsEnabled,
              templateUrl: 'myModalContent.html',
              controller: 'ModalInstanceCtrl',
              //size: size,
              resolve: {
                alarm: function () {
                  return alarm;
                }
              }
            });

            modalInstance.result.then(function(formData) {
                $scope.updateAlarm(formData);
            })
        };
    }])

    .controller('ModalInstanceCtrl', function ($scope, $uibModalInstance, $http, alarm) {
        $scope.mytime = new Date();
        $scope.hstep = 1;
        $scope.mstep = 15;
        $scope.ismeridian = true;
        $scope.formData = alarm;

        $scope.cancel = function () {
            $uibModalInstance.dismiss('cancel');
        };

        $scope.ok = function () {
            $scope.formData.status =1; // by default status of all new alarms is kept as 1
            $uibModalInstance.close($scope.formData);
        };

    });