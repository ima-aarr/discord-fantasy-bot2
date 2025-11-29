import datetime
from core import db, audit

def create_country(user_id,name):
    path=f'countries/{user_id}'
    if db.get(path): return False,'exists'
    state={'owner':user_id,'name':name,'population':100}
    db.put(path,state); audit.log('create_country', user_id, {'name':name}); return True,state

def get_country(user_id): return db.get(f'countries/{user_id}')
