from bottle import *

# from bottle import route, run


@route('/hello')
def hello():
    return "Hello World!"

@error(404)
def error404(error):
    return 'wrong, 404!'

run(host='localhost', port=8080, debug=True)
