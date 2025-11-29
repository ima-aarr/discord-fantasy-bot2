import random
from core import db, audit

def create_adventurer(server_id, owner_id, name, cls, desc=''):
    aid=f'adv_{owner_id}_{int(random.random()*1e9)}'
    adv={'id':aid,'owner':owner_id,'name':name,'class':cls,'desc':desc,'stats':{'HP':50}}
    db.put(f'worlds/{server_id}/adventurers/{aid}', adv)
    audit.log('create_adventurer', owner_id, {'adv':aid})
    return adv
