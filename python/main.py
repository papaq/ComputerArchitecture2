from bottle import *

# from bottle import route, run


@route('/hello')
def hello():
    return "Hello!"


@error(404)
def error404():
    return 'wrong, 404!'


@get('/server')
def visit_server():
    return static_file('server.html', root='./')


@get('/server')
def visit_server():
    return static_file('client.html', root='./')


run(host='localhost', port=8080, debug=True)
