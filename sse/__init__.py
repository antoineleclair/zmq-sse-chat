from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from sse.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'sse:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('events', '/events')
    config.add_route('push', '/push/{channel}')
    config.scan('sse')
    return config.make_wsgi_app()

