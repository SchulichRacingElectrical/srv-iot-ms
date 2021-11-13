# Copyright Schulich Racing FSAE
# Written By Justin Tijunelis

import os
import redis

class Publisher:
  def __init__(self):
    url = os.getenv('REDIS_URL')
    port = os.getenv('REDIS_PORT')
    self.redis_db = redis.Redis(host=url, port=port, db=0)

  def publish_snapshot(self, api_key, snapshot):
    pass

publisher = Publisher()