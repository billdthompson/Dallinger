"""Heroku web worker."""

from future.builtins import map
import os

import redis
from rq import (
    Worker,
    Queue,
    Connection
)

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url, decode_responses=True)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
