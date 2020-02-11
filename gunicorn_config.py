"""gunicorn WSGI server configuration."""
from os import environ

HOST = '0.0.0.0'
PORT = 8501

bind = HOST + ':' + environ.get('PORT', str(PORT))
max_requests = 10000
worker_class = 'gevent'
workers = 4
timeout = 5
keep_alive = 5