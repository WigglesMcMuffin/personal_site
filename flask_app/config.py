import os

def get_database_uri(testing=False):
  if testing:
    return 'postgresql://postgres@db/web_games_test'
  else:
    return 'postgresql://postgres@db/web_games'

def get_datastore_uri(testing):
  return {'data-store': 'monetdb://monetdb@test-data-store'}
  return {'data-store': 'monetdb://monetdb@data-store'}
