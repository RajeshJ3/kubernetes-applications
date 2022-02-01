from fastapi import FastAPI
from redis import Redis

import os

# FastAPI app object
app = FastAPI()

# Redis credentials from os
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

# redis db instance
cache = Redis(host=REDIS_HOST, port=REDIS_PORT)

# GET route at root
@app.get("/")
def index():
    message = cache.get('message')
    return {'detail': message}

# POST route at root
@app.post("/")
def index(message: str = 'Hello, World!', ttl: int = 10):
    cache.set('message', message, ex=ttl)
    return {'detail': 'succcess'}
