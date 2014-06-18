var movies_app = angular.module('movies_app', []);
var HOST = "http://54.213.58.239:5001/api/v1/";

movies_app.controller('GetAllMovies', ['$scope', '$http',
    function ($scope, $http) {
        $http
            .get(HOST + 'movies/')
            .success(function (data, status, headers, config) {
                $scope.movies = data;
            });

        $scope.resetNotifications = function (){
            $scope.success_notification = null;
            $scope.error_notification = null;
        };

        $scope.loginClicked = function () {
            $scope.resetNotifications();
            $http
                .post(HOST + 'login/',
                {
                    'username': $scope.username,
                    'password': $scope.password
                })
                .success(function (data, status, headers, config) {
                    $scope.token = data;
                    $scope.success_notification = 'Login Successful';
                });
        };

        $scope.searchClicked = function () {
            $scope.resetNotifications();

            $http
                .get(HOST + 'movies/search/' + $scope.searchText)
                .success(function (data, status, headers, config) {
                    $scope.movies = data;
                    $scope.edit_movie_details_present = false;
                    $scope.searchResult = "Showing " + data.length + " results for: " + $scope.searchText;
                });
        };

        $scope.editClicked = function (slug) {
            $scope.resetNotifications();
            $scope.old_slug = slug;
            $http
                .get(HOST + 'movie/' + slug + '/', {

                })
                .success(function (data, status, headers, config) {
                    $scope.edit_movie_details_present = true;
                    $scope.edit_movie = data;
                    $scope.movies = [];
                });
        };

        $scope.saveMovie = function () {
            $scope.resetNotifications();
            if ($scope.token == undefined) {
                $scope.token = "random_string_wont_be_found";
            }

            if ($scope.old_slug != undefined) {
                $http
                    .post(HOST + 'movie/' + $scope.edit_movie['slug'] + '/',
                    {
                        'data': $scope.edit_movie,
                        'token': $scope.token
                    })
                    .success(function (data, status, headers, config) {
                        $scope.success_notification = "Movie successfully edited";
                        $http
                            .get(HOST + 'movies/')
                            .success(function (data, status, headers, config) {
                                $scope.edit_movie_details_present = false;
                                $scope.movies = data;
                            });
                    })
                    .error(function (data, status, headers, config) {
                        $scope.error_notification = "You are not an admin. Only admins are allowed to edit. Please login using password=admin";
                    });
            }
            else {
                $http
                    .put(HOST + 'movie/new/',
                    {
                        'data': $scope.edit_movie,
                        'token': $scope.token
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
            $scope.resetNotifications();
            if ($scope.token == undefined) {
                $scope.token = "random_string_wont_be_found";
            }

            $http
                .delete(HOST + 'movie/' + slug + '/?token=' + $scope.token,
                {
                    'token': $scope.token
                })
                .success(function (data, status, headers, config) {
                    $scope.success_notification = "Movie successfully deleted";
                    $http
                        .get(HOST + 'movies/')
                        .success(function (data, status, headers, config) {
                            $scope.movies = data;
                        });
                })
                .error(function (data, status, headers, config) {
                    $scope.error_notification = "You are not a super_admin. Only admins are allowed to delete. Please login using password=super_admin";
                });

        };
    }]);