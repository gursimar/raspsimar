/**
 * Created by Gursimran on 05-Mar-16.
 */

var app = angular.module("app", [
    'ui.router'
]);

app.controller('AppCtrl', function($http) {
	var app = this;
	app.message = "Am i working";

    $http.get("/api/video").success(function(data) {
        app.videos = data.objects;

    })

    app.addVideo = function () {
        $http.post("/api/video/", {"title":"now", "image":"abc.png"})
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
