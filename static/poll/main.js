/*globals $, document, WebSocket, initScene, animateScene, toString, dataValues */
/*jslint devel: true */

$(function () {
    "use strict";
    $(document).ready(function () {

        var ws, option, i, o, host = "10.1.1.24", port = "8888", uri = '/ws', schema;
        ws = new WebSocket("ws://" + host + ":" + port + uri);
        
        ws.onmessage = function (evt) {
            console.log("server: " + evt.data);
            var data = $.parseJSON(evt.data);
            console.log(data.status);
            if (data.status === "ok") {
                console.log("receipt: " + data.status);
                $(option).css("background", "#00ff00");
                if (data.latest) {
                    if (document.title === "modprods poll results") {
                        console.log(dataValues);
                        o = data.latest[0];
                        dataValues = [[o[0], o[1], o[2], o[3], o[4]]];
                        initScene();
                    }
                }
            } else if (data.status === 'nok') {
                console.log("receipt: " + data.status);
                $(option).css("background", "#ff0000");
            } else {
                ws = new WebSocket("ws://" + host + ":" + port + uri);
            }
        };

        ws.onclose = function (evt) { console.log("Connection close"); };

        ws.onopen = function (evt) {
        };
             
        document.ontouchmove = function (e) {
            e.stopPropagation();
        };
        
        $('button').click(function () {
            console.log("clicked (" + $(this).attr('id') + ")");
            $("button").css("background", "#ffffff");
            $("#text").css("background", "#ffffff");
            option = "#" + $(this).attr('id');
            ws.send("/vote/" + $(this).attr('id'));
        });
        
        $("#theForm").submit(function () {
            console.log("submit message " + $("#text").attr("value"));
            $("button").css("background", "#ffffff");
            $("#text").css("background", "#ffffff");
            ws.send("/message/" + $("#text").attr("value"));
            return false;
        });

        $("button").click(function (evt) {
            evt.preventDefault();

        });
    }
        );
}
    );
