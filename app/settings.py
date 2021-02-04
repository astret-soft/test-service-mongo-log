""" Settings
"""
from os import environ as env

MONGODB_HOST = env.get('MONGODB_HOST', default='mongodb://127.0.0.1:27017')
WS_LOG_SRC = env.get('WS_LOG_SRC', default='ws://127.0.0.1:8080')
WS_RETRIES_TIMEOUT = int(env.get('WS_RETRIES_TIMEOUT', default=5))
HOST = env.get('HOST', default='0.0.0.0')
PORT = int(env.get('PORT', default=65333))
