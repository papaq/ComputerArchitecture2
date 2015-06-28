from bottle import *
import json
import uuid

from defs import *

substring = ""
main_string = ""
clients = []
tasks = []
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
    global tasks
    global substring, main_string
    substring = request.forms.get('substring')
    main_string = request.forms.get('main_string')
    if len(substring) > len(main_string):
        return json.dumps({'task_was_done': True,
                          'result': "Check Your laces"})
    if done_tasks:
        for i in xrange(len(done_tasks)):
            if (done_tasks[i]["task"][0] == substring &
                done_tasks[i]["task"][1] == main_string):
                return json.dumps({'task_was_done': True,
                                  'result': done_tasks[i]["result"]})

    a_len = len(substring)
    tasks = prepair_tasks(devide_into_substrings(a_len, main_string, 5 * a_len), substring)
    return json.dumps({'task_was_done': False})


@get("/tasks/done")
def calculate_done():
    global tasks
    done = 0
    if not tasks:
        return 100
    for task in tasks:
        if task["done"]:
            done += 1
    return json.dumps({'done': done * 100 / len(tasks)})


@get("/clients/new_client")
def add_new_client():
    name = uuid.uuid4()
    new_client(clients, str(name))
    return json.dumps({'name': str(name)})


@get("/clients/last_client")
def show_last_client():
    return json.dumps({'name': clients[len(clients) - 1]["name"]})


@get("/c_worker.js")
def visit_worker():
    return static_file('c_worker.js', root='../js/')


@get("/clients/here/<client_name>")
def update_client(client_name=""):
    print(str(len(clients)))
    if client_name == "":
        return
    new_client(clients, client_name)
    print(str(len(clients)) + "  " + client_name)
    return "OK"


@get("tasks/get_task")
def give_task():
    return


run(host='localhost', port=8081, debug=True)
