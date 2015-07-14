/**
 * Created by liuzheng on 7/9/15.
 */
'use strict';
var NgApp = angular.module('App', ['']);
NgApp.config(function($interpolateProvider){
  $interpolateProvider.startSymble('{[{');
  $interpolateProvider.endSymble('}]}');
});
// routeProvider
//function($routeProvider, $rootScope){
//  $routeProvider.
//    when('/',{
//      templateUrl: 'main.html',
//      controller: 'Index'
//    }).
//    when('/',{
//      templateUrl: 'main.html',
//      controller: 'Index'
//    });
//}
