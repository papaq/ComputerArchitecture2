from bottle import *
import json

clients = 1

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


@get('/server.css')
def visit_server():
    return static_file('server.css', root='../html_css/')

@get("/clients/count")
def get_clients_count():
    return json.dumps({'count': clients})

run(host='localhost', port=8080, debug=True)
