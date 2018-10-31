# -*- coding: utf-8 -*-

bind = '0.0.0.0:5000'
workers = 3
worker_class = 'eventlet'

max_requests = 1024 * 10
max_requests_jitter = max_requests

accesslog = None
errorlog = '-'
