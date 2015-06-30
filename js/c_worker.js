/**
 * Created by solomon on 26.06.15.
 */

var client_name = "";
var xmlhttp = new XMLHttpRequest();
receive_respond_and_do = function () {
};
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

post_request = function (url, data, respond_and_do) {
    receive_respond_and_do = respond_and_do;
    xmlhttp.open("POST", url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    xmlhttp.send(data);
};

n_times_a_in_b = function (a, b) {
    var times = 0;
    for (var i = 0; i < b.length - a.length + 1; i++) {
        if (b.substr(i, a.length) == a) {
            times++;
        }
    }
    return times;
};

(function set_name() {
    get_request("/clients/last_client", function (respond_text) {
        client_name = JSON.parse(respond_text).name;
    });
})();

setInterval(function im_here() {
    get_request("/clients/here/" + client_name, function () {
    })
}, 1500);

setInterval(function i_wanna_work() {
    var answer = "";
    var task = undefined;
    get_request("/tasks/get_task", function (respond_text) {
        task = JSON.parse(respond_text);
        console.log(task);

        if (task === undefined || task == "nothing_to_do")
            return;

        answer = "task_number=" + task.number +
            "&result=" + n_times_a_in_b(task.substring, task.main_string);

        console.log(answer);
        post_request("/tasks/post_result", encodeURI(answer), function () {
        });
    });

}, 600);
