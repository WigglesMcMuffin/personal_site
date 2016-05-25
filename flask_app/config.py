import os

def get_database_uri():
  return 'postgresql://postgres@db/web_games'

def get_datastore_uri():
  return {'data-store': 'monetdb://monetdb@data-store'}
