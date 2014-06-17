var movies_app = angular.module('movies_app', []);
var HOST = "http://localhost:5001/api/v1/";

movies_app.controller('GetAllMovies', ['$scope', '$http',
    function ($scope, $http) {
        $http
            .get(HOST + 'movies/')
            .success(function (data, status, headers, config) {
                $scope.movies = data;
            });

        $scope.searchClicked = function () {
            $http
                .get(HOST + 'movies/search/' + $scope.searchText)
                .success(function (data, status, headers, config) {
                    $scope.movies = data;
                    $scope.edit_movie_details_present = false;
                    $scope.searchResult = "Showing " + data.length + " results for: " + $scope.searchText;
                });
        };

        $scope.editClicked = function (slug) {
            $scope.slug = slug;
            $http
                .get(HOST + 'movie/' + slug + '/')
                .success(function (data, status, headers, config) {
                    $scope.edit_movie_details_present = true;
                    $scope.edit_movie = data;
                    $scope.movies = [];
                });
        };

        $scope.saveMovie = function(){

        };

        $scope.deleteClicked = function (slug) {
            $http
                .get(HOST + 'movie/' + slug + '/')
                .success(function (data, status, headers, config) {
                    console.log(data);
                    console.log(status);
                });
        };

    }]);