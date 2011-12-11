import datetime, time, zmq, json
from pyramid.view import view_config
from pyramid.response import Response

SOCK = 'ipc:///tmp/zmq.test'
context = zmq.Context()

@view_config(route_name='home', renderer='/home.mako')
def home(request):
    return {}
    
@view_config(route_name = 'events')
def events(request):
    headers = [('Content-Type', 'text/event-stream'),
               ('Cache-Control', 'no-cache')]
    response = Response(headerlist=headers)
    response.app_iter = time_generator()
    return response
    
@view_config(route_name = 'push')
def push(request):
    msg = request.json_body['message']

    socket = context.socket(zmq.PUB)
    socket.bind(SOCK)
    socket.send(msg.encode('utf-8'))

    return Response()

def time_generator():
    while True:
        yield "data: %s\n\n" % str(datetime.datetime.now())
        time.sleep(600)

