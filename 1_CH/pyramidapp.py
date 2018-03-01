'''
Author: Tayloc Cochran
Project: NATS
Goal:
  Set up a fake pyramid app
'''


from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
  return Response(
    "Hello World from Pyr1\n",
    content_type="text/plain"
    )

config = Configurator()
config.add_route("hello", "/hello")
config.add_view(hello_world, route_name='hello')
app = config.make_wsgi_app()