/**
 * Created by Gursimran on 05-Mar-16.
 */

var app = angular.module("app", [
    'ui.router', 'ui.bootstrap'
])
    .config(['$urlRouterProvider', '$stateProvider', function($urlRouterProvider, $stateProvider) {
        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state('home', {
                url:'/',
                templateUrl:'home.html',
                controller: 'homeCtrl'
            })
            .state('about', {
                url:'/about',
                templateUrl:'about.html',
                controller: 'aboutCtrl'
            })
            .state('alarm', {
                url:'/alarm',
                templateUrl:'alarm.html',
                controller: 'alarmCtrl'
            })
    }])

app.controller('AppCtrl', function($http, $scope) {
	var app = this;
	app.message = "Am i working";
    $scope.isCollapsed = false;

    $http.get("/api/video").success(function(data) {
        app.videos = data.objects;

    })

    app.addVideo = function () {
        $http.post("/api/video", {"title":"adnow", "image":"assbc.png"})
        .success(function (data) {
                app.videos.push(data);
        })
    }

    app.deleteVideo  =function (video) {
        $http.delete("/api/video/" + video.id).success(function (response) {
            app.videos.splice(app.videos.indexOf(video),1)
        })
    }
})
