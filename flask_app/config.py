import os

def get_database_uri(testing=False):
  if testing:
    return 'postgresql://postgres@db/web_games_test'
  else:
    return 'postgresql://postgres@db/web_games'

def get_datastore_uri(testing=False):
  if testing:
    return {'data-store': 'monetdb://monetdb@data_store/test-data-store'}
  else:
    return {'data-store': 'monetdb://monetdb@data_store/data-store'}
