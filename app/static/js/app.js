var movies_app = angular.module('movies_app', []);
var HOST = "http://54.213.58.239:5001/api/v1/";

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
            $scope.old_slug = slug;
            $http
                .get(HOST + 'movie/' + slug + '/')
                .success(function (data, status, headers, config) {
                    $scope.edit_movie_details_present = true;
                    $scope.edit_movie = data;
                    $scope.movies = [];
                });
        };

        $scope.saveMovie = function () {
            console.log($scope.old_slug);

            if ($scope.old_slug != undefined) {
                $http
                    .post(HOST + 'movie/' + $scope.edit_movie['slug'] + '/',
                    {
                        'data': $scope.edit_movie
                    })
                    .success(function (data, status, headers, config) {
                        $scope.success_notification = "Movie successfully edited";
                        $http
                            .get(HOST + 'movies/')
                            .success(function (data, status, headers, config) {
                                $scope.edit_movie_details_present = false;
                                $scope.movies = data;
                            });
                    });
            }
            else {
                $http
                    .put(HOST + 'movie/new/',
                    {
                        'data': $scope.edit_movie
                    })
                    .success(function (data, status, headers, config) {
                        $scope.success_notification = "Movie successfully added";
                        $http
                            .get(HOST + 'movies/')
                            .success(function (data, status, headers, config) {
                                $scope.edit_movie_details_present = false;
                                $scope.movies = data;
                            });
                    });
            }

            $scope.old_slug = null;
        };

        $scope.deleteClicked = function (slug) {
            $http
                .delete(HOST + 'movie/' + slug + '/')
                .success(function (data, status, headers, config) {
                    $scope.success_notification = "Movie successfully deleted";
                    $http
                        .get(HOST + 'movies/')
                        .success(function (data, status, headers, config) {
                            $scope.movies = data;
                        });
                });
        };
    }]);