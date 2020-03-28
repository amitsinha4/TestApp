""" Cherry Py Server """
from cheroot.wsgi import Server as WSGIServer
from manage import app

# Configuring the WSGI Server
server = WSGIServer(bind_addr=("0.0.0.0", 5000), wsgi_app=app, numthreads=100)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()
