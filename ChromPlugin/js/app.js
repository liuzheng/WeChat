/**
 * Created by liuzheng on 7/17/15.
 */
'use strict';
var app = angular.module('app', []);
app.controller('Ctrl', function ($scope) {
    if (localStorage.getItem('isOK') == 'true') {
        document.getElementById('wxSwitch').checked = true
    } else {
        document.getElementById('wxSwitch').checked = false
    }
    $scope.Switch = function (target) {
        //var target  = $("#wxSwitch");
        console.log(localStorage.getItem('isOK'))
        if (localStorage.getItem('isOK') == 'true') {
            localStorage.setItem('isOK', false);
            document.getElementById(target).checked = false
        } else {
            localStorage.setItem('isOK', true);
            document.getElementById(target).checked = true
        }
    };
});