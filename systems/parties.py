import random
from core import db, audit

def create_party(server_id, leader_adv):
    pid=f'party_{int(random.random()*1e9)}'; party={'id':pid,'leader':leader_adv,'members':[leader_adv]}
    db.put(f'worlds/{server_id}/parties/{pid}', party); audit.log('create_party', leader_adv, {'party':pid}); return party
