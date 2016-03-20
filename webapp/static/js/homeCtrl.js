/**
 * Created by Gursimran on 20-Mar-16.
 */

angular
    .module('app')
    .controller('homeCtrl', ['$scope', '$http', function ($scope, $http) {
        $scope.title = "Home - simar"

        $http.get("/api/video").success(function(data) {
            $scope.videos = data.objects;

        })

        app.addVideo = function () {
            $http.post("/api/video", {"title":"now", "image":"abc.png"})
            .success(function (data) {
                    app.videos.push(data);
            })
        }

        app.deleteVideo  =function (video) {
            $http.delete("/api/video/" + video.id).success(function (response) {
                app.videos.splice(app.videos.indexOf(video),1)
            })
        }
    }])