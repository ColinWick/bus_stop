import pandas as pd
import yaml
import requests
from google.transit import gtfs_realtime_pb2 as gtfs

with open('config.yml','r') as yamlfile:
    config = yaml.safe_load(yamlfile)

req = requests.get(config['train-apis']['ACE'])

feed = gtfs.FeedMessage()
feed.ParseFromString(req.content)
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)