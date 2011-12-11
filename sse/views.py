import datetime, time, zmq, json, threading
from pyramid.view import view_config
from pyramid.response import Response

SOCK = 'ipc:///tmp/zmq.test'
context = zmq.Context()

pub_socket = context.socket(zmq.PUB)
pub_socket.bind(SOCK)

pub_lock = threading.Lock()

@view_config(route_name='home', renderer='/home.mako')
def home(request):
    return {}
    
@view_config(route_name = 'events')
def events(request):
    headers = [('Content-Type', 'text/event-stream'),
               ('Cache-Control', 'no-cache')]
    response = Response(headerlist=headers)
    response.app_iter = message_generator()
    return response
    
@view_config(route_name = 'push')
def push(request):
    msg = json.loads(request.body)['message']
    with pub_lock:
        pub_socket.send(msg.encode('utf-8'))
    return Response()

def message_generator():
    socket2 = context.socket(zmq.SUB)
    socket2.connect(SOCK)
    socket2.setsockopt(zmq.SUBSCRIBE, '')
    while True:
        msg = socket2.recv()
        yield "data: %s\n\n" % json.dumps({'message': msg})
