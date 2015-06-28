/**
 * Created by solomon on 26.06.15.
 */

client_name = "";
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

post_request = function (url, data, respond_and_do) {
    receive_respond_and_do = respond_and_do;
    xmlhttp.open("POST", url, true);
    //obj.xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    xmlhttp.send(data);
};

(function set_name(){
    get_request("/clients/last_client", function(respond_text){
        client_name = JSON.parse(respond_text).name;
    })
})();

setInterval(function im_here(){
    get_request("clients/here/" + client_name, function(){})
}, 1000);


