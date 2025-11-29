import json, random
from core import db, audit
async def explore(server_id, adv_id):
    adv=db.get(f'worlds/{server_id}/adventurers/{adv_id}')
    if not adv: return {'ok':False,'error':'no_adv'}
    evt={'type':'monster','narration':'wolf encountered'}
    db.post(f'worlds/{server_id}/events', {'adv':adv_id,'event':evt}); return {'ok':True,'event':evt}
