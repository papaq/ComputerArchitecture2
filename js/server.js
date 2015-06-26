/**
 * Created by solomon on 25.06.15.
 */

var substring = "";
var main_string = "";

function random_fill(n){
    var random_string = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for(var i=0; i < n; i++){
        random_string += possible.charAt(Math.floor(Math.random() * possible.length));
    }

    return random_string;
}

function set_strings(string1, string2){
    substring = string1;
    main_string = string2;
}

function post_smth(url, data, callback){

}

function post_task(){
    set_strings(document.getElementById("substring"), document.getElementById("main_string"));
}
