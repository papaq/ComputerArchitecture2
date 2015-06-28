from bottle import *
import json
import uuid

from defs import *

substring = ""
main_string = ""
clients_count = 1
clients = []
done_tasks = []


@route('/hello')
def hello():
    return "Hello!"


@error(404)
def error404(_error):
    return 'wrong, 404!'


@route('/server')
def visit_server():
    return static_file('server.html', root='../html_css/')


@get('/client')
def visit_server():
    return static_file('client.html', root='../html_css/')


@get('/js/server.js')
def visit_server():
    return static_file('server.js', root='../js/')


@get('/js/client.js')
def visit_server():
    return static_file('client.js', root='../js/')


@get('/server.css')
def visit_server():
    return static_file('server.css', root='../html_css/')


@get("/clients/count")
def get_clients_count():
    update_workers(clients)
    print(len(clients))
    print(clients)
    return json.dumps({'count': len(clients)})


@post("/tasks/new_task")
def add_new_task():
    global substring, main_string
    substring = request.forms.get('substring')
    main_string = request.forms.get('main_string')

    return json.dumps({'task_was_done': True},
                      {'result': 10})


@get("/clients/new_client")
def add_new_client():
    name = uuid.uuid4()
    clients.append({"name": str(name), "seen": time()})
    return json.dumps({'name': str(name)})


@get("/clients/last_client")
def show_last_client():
    return json.dumps({'name': clients[len(clients)-1]["name"]})


@get("/c_worker.js")
def visit_worker():
    return static_file('c_worker.js', root='../js/')


@get("/clients/here/<client_name>")
def update_client(client_name=""):
    print(str(len(clients)))
    if client_name == "":
        return
    index = find_vocabulary_by_field(clients, "name", client_name)
    if index == -1:
        clients.append({"name": client_name, "seen": time()})
    else:
        clients[index]["seen"] = time()
    print(str(len(clients)) + "  " + client_name)
    return


run(host='localhost', port=8081, debug=True)
