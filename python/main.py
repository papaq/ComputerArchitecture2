from bottle import *
import json
import uuid

from defs import *

substring = ""
main_string = ""
clients = []
tasks = []
done_tasks = []
result = 0


@error(404)
def error404(_error):
    """
    Tracking 404-error pages
    :param _error: error
    :return: message about trouble
    """
    return 'wrong, 404!'


@route('/client')
def visit_client():
    """
    Tracking client-page requests
    :return: client web-page
    """
    return static_file('client.html', root='../html_css/')


@get('/worker')
def visit_worker():
    """
    Tracking worker-page requests
    :return: worker web-page
    """
    return static_file('worker.html', root='../html_css/')


@get('/js/client.js')
def get_client_js():
    return static_file('client.js', root='../js/')


@get('/js/worker.js')
def get_worker_js():
    """
    Tracking worker.js file requests
    :return: worker.js file
    """
    return static_file('worker.js', root='../js/')


@get('/client.css')
def get_client_css():
    """
    Tracking client.css file requests
    :return: client.css file
    """
    return static_file('client.css', root='../html_css/')


@get("/clients/count")
def get_clients_count():
    """
    Tracking clients amount request
    Updating clients list
    :return: clients amount
    """
    update_workers(clients)
    return json.dumps({'count': len(clients)})


@post("/tasks/new_task")
def add_new_task():
    """
    Tracking requests on adding new task
    Dividing task into parts
    :return: result, if this task was executed earlier
    """
    global tasks, result
    global substring, main_string
    substring = request.forms.get('substring')
    main_string = request.forms.get('main_string')
    if len(substring) > len(main_string):
        return json.dumps({'task_was_done': True,
                           'result': "Check Your laces"})
    if done_tasks:
        for i in xrange(len(done_tasks)):
            if done_tasks[i]["strings"][0] == substring and done_tasks[i]["strings"][1] == main_string:
                return json.dumps({'task_was_done': True,
                                   'result': done_tasks[i]["result"]})

    result = 0
    a_len = len(substring)
    tasks = prepair_tasks(devide_into_substrings(a_len, main_string, 5 * a_len), substring)
    return json.dumps({'task_was_done': False})


@get("/tasks/done")
def calculate_done():
    """
    Tracking requests on task execution process
    :return: <done parts> * 100 / <all parts>
    """
    global tasks
    done = 0
    if not tasks:
        return 100
    for task in tasks:
        if task["done"] == 2:
            done += 1
    return json.dumps({'done': done * 100 / len(tasks)})


@get("/clients/new_client")
def add_new_client():
    """
    Tracking new client adding requests
    :return: unique client name
    """
    name = uuid.uuid4()
    new_client(clients, str(name))
    return json.dumps({'name': str(name)})


@get("/c_worker.js")
def visit_worker():
    """
    Tracking c_worker.js file request
    :return: c_worker.js file
    """
    return static_file('c_worker.js', root='../js/')


@get("/clients/here/<client_name>")
def update_client(client_name=""):
    """
    Tracking clients saying "hi!"-requests
    :param client_name: name of client
    :return: "OK"
    """
    if client_name == "":
        return
    new_client(clients, client_name)
    return "OK"


@get("/tasks/get_task")
def give_task():
    """
    Tracking task request
    Marking the task as "in process"
    :return: task
    """
    global tasks
    if not tasks:
        return json.dumps("nothing_to_do")
    for task in tasks:
        if task["done"] == 0:
            task["done"] = 1
            return json.dumps({"number": task["number"],
                               "substring": task["strings"][0],
                               "main_string": task["strings"][1]})
    for task in tasks:
        if task["done"] == 1:
            return json.dumps({"number": task["number"],
                               "substring": task["strings"][0],
                               "main_string": task["strings"][1]})

    return json.dumps("nothing_to_do")


@post("/tasks/post_result")
def get_result():
    """
    Tracking result-posting request
    Marking the task as "done"
    :return: "OK"
    """
    global tasks, result
    task_number = int(request.forms.get('task_number'))
    _result = int(request.forms.get('result'))

    if tasks:
        if len(tasks) > task_number:
            if tasks[task_number]["done"] != 2:
                tasks[task_number]["done"] = 2
                result += _result
    return "OK"


@get("/tasks/result")
def task_result():
    """
    Tracking result-getting request
    Updating list with done tasks
    :return: result
    """
    global tasks, done_tasks
    done_tasks.append({"strings": [substring, main_string],
                       "result": result})

    return json.dumps({"result": result})


run(host='localhost', port=8081, debug=True)
