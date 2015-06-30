/**
 * Created by solomon on 25.06.15.
 */

var server_object = server_object || {};

(function (obj) {
    obj.xmlhttp = null;
    obj.receive_respond_and_do = function () {
    };
    obj.main_string = "";
    obj.substring = "";

    function set_strings(string1, string2) {
        obj.substring = string1;
        obj.main_string = string2;
    }

    obj.request = function () {
        if (obj.xmlhttp === null) {
            obj.xmlhttp = new XMLHttpRequest();
            obj.xmlhttp.onreadystatechange = function () {
                if (obj.xmlhttp.readyState === 4 && obj.xmlhttp.status === 200) {
                    obj.receive_respond_and_do(obj.xmlhttp.responseText);
                }
            }
        }
    };

    obj.get_request = function (url, receive_respond_and_do) {
        obj.receive_respond_and_do = receive_respond_and_do;
        obj.xmlhttp.open("GET", url, true);
        obj.xmlhttp.send();
    };

    obj.post_request = function (url, data, receive_respond_and_do) {
        obj.receive_respond_and_do = receive_respond_and_do;
        obj.xmlhttp.open("POST", url, true);
        //obj.xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
        obj.xmlhttp.send(data);
    };

    document.getElementById("start").addEventListener("click", function () {
        document.getElementById("start").disabled = true;
        document.getElementById("done").innerText = "0%";
        document.getElementById("result").value = "";

        set_strings(document.getElementById("substring").value, document.getElementById("main_string").value);
        if (obj.substring == "" || obj.main_string == "") {
            document.getElementById("result").value = obj.substring + "=0";
            document.getElementById("start").disabled = false;
        }
        else {

            var post_data = "substring=" + obj.substring + "&main_string=" + obj.main_string;

            obj.post_request('/tasks/new_task', encodeURI(post_data), function (respond_text) {
                var json = JSON.parse(respond_text);
                if (json.task_was_done) {
                    document.getElementById("result").value = obj.substring + "=" + json.result +
                                                              "\ntime=" + json.time + " seconds";
                    document.getElementById("start").disabled = false;
                    document.getElementById("done").innerText = "100%";
                }

                else {
                    var myVar = setInterval(function () {
                        var done = 0;
                        obj.get_request('/tasks/done', function (respond_text) {
                            var json = JSON.parse(respond_text);
                            done = json.done;
                            document.getElementById("done").innerText = done + "%";

                            if (done == 100) {
                                obj.get_request('/tasks/result', function (respond_text) {
                                    var json = JSON.parse(respond_text);
                                    document.getElementById("result").value = obj.substring + "=" + json.result +
                                                                              "\ntime=" + json.time + " seconds";
                                    document.getElementById("start").disabled = false;
                                    clearInterval(myVar);
                                })
                            }
                        });
                    }, 1800);

                }
            });

        }
    });

    obj.request();


    setInterval(function () {
        obj.get_request('/clients/count', function (respond_text) {
            var json = JSON.parse(respond_text);
            document.getElementById("n_clients").innerText = json.count;
        })
    }, 2000)

})(server_object);
