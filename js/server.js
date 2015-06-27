/**
 * Created by solomon on 25.06.15.
 */

function random_fill(n){
    var random_string = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for(var i=0; i < n; i++){
        random_string += possible.charAt(Math.floor(Math.random() * possible.length));
    }

    return random_string;
}

var server_object = server_object || {};

(function(obj){
    obj.xmlhttp = null;
    obj.receive_respond_and_do = null;
    obj.web_worker = null;
    obj.main_string = "";
    obj.substring = "";

    function set_strings(string1, string2){
        obj.substring = string1;
        obj.main_string = string2;
    }

    obj.request = function(){
        if (obj.xmlhttp === null){
            obj.xmlhttp = new XMLHttpRequest();
            obj.xmlhttp.onreadystatechange = function() {
                obj.receive_respond_and_do(obj.xmlhttp.responseText);
            }
        }
    };

    obj.get_request = function(url, receive_respond_and_do){
        obj.xmlhttp.open("GET", url, true);
        obj.receive_response_and_do = receive_respond_and_do;
        obj.xmlhttp.send();
    };

    obj.post_request = function(url, data, receive_respond_and_do){
        obj.xmlhttp.open("POST", url, true);
        obj.receive_response_and_do = receive_respond_and_do;
        //obj.xmlhttp.setRequestHeader()
        obj.xmlhttp.send(data);
    };

    document.getElementById("start").addEventListener("click", function (){
        document.getElementById("done").innerText = "00%";
        document.getElementById("result").value = "";
        console.log("hi");

        set_strings(document.getElementById("substring").value, document.getElementById("main_string").value);
        if (obj.substring == "" || obj.main_string == ""){
            document.getElementById("result").value = obj.substring + "=0";
            return;
        }
        else{
            console.log("Ku");

            var post_data = "str_in" + obj.substring + "&str_full" + obj.main_string;

            obj.post_request('/tasks/new_task', encodeURI(post_data), function(respond_text){
                var json = JSON.parse(respond_text);
                if (json.task_was_done){
                    document.getElementById("result").value = obj.substring + "=" + json.result;
                    return;
                }
                else{
                    var done = 0;
                    while (done < 100){
                        obj.get_request('/tasks/done', function(respond_text){
                            var json = JSON.parse(respond_text);
                            done = json.done;
                            document.getElementById("done").innerText = done + "%";
                        });

                        sleep(1000);
                    }
                }
            });

        }
    });

    obj.request();

    setInterval(function() {
        obj.get_request('/clients/count', function(respond_text){
            var json = JSON.parse(respond_text);
            document.getElementById("n_clients").innerText = json.count;
        })
    }, 1000)

})(server_object);
