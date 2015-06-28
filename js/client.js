/**
 * Created by solomon on 25.06.15.
 */

//var client_object = client_object || {};

xmlhttp = new XMLHttpRequest();
receive_respond_and_do = function(){};
xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
                receive_respond_and_do(xmlhttp.responseText);
            }
        };

get_request = function (url, respond_and_do) {
    receive_respond_and_do = respond_and_do;
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
};

window.onload = function () {
    get_request("/clients/new_client", function (respond_text) {
        document.getElementById("client_name").innerText = JSON.parse(respond_text).name;
    });
    web_worker = new Worker("/c_worker.js")
};
