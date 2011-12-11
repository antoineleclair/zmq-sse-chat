import datetime, time
from pyramid.view import view_config
from pyramid.response import Response


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
    
def time_generator():
    while True:
        yield "data: %s\n\n" % str(datetime.datetime.now())
        time.sleep(600)

