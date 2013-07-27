/*globals $, document, WebSocket */
/*jslint devel: true */

$(function () {
    "use strict";
    $(document).ready(function () {

        var ws, host = "10.1.1.24", port = "8888", uri = '/ws';

        ws = new WebSocket("ws://" + host + ":" + port + uri);

        ws.onmessage = function (evt) {console.log("server: " + evt.data); };

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
            var option = "#" + $(this).attr('id'), ok = false;
            ws.send("/vote/" + $(this).attr('id'));
            ws.onmessage = function (evt) {
                if (evt.data === "ok") {
                    console.log("receipt: " + evt.data);
                    $(option).css("background", "#00ff00");
                    ok = true;
                }
            };
            if (ok !== true) {
                $(option).css("background", "#000000");
                ws = new WebSocket("ws://" + host + ":" + port + uri);
            }
        });
        
        $("#theForm").submit(function () {
            console.log("submit message " + $("#text").attr("value"));
            $("button").css("background", "#ffffff");
            $("#text").css("background", "#ffffff");
            ws.send("/message/" + $("#text").attr("value"));
            var ok = false;
            ws.onmessage = function (evt) {
                if (evt.data === "ok") {
                    console.log("receipt: " + evt.data);
                    $("#text").css("background", "#00ff00");
                    ok = true;
                }
            };
            if (ok !== true) {
                $("#text").css("background", "#000000");
                ws = new WebSocket("ws://" + host + ":" + port + uri);
            }
            return false;
        });

        $("button").click(function (evt) {
            evt.preventDefault();

        });
    }
        );
}
    );
