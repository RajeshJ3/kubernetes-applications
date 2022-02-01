from fastapi import FastAPI
from redis import Redis

import os

app = FastAPI()

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

cache = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.get("/")
def index():
    message = cache.get('message')
    return {'detail': message}

@app.post("/")
def index(message: str = 'Hello, World!', ttl: int = 10):
    cache.set('message', message, ex=ttl)
    return {'detail': 'succcess'}
