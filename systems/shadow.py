from core import db, audit

def hire_lieutenant(country_id,name,desc=''):
    c=db.get(f'countries/{country_id}')
    if not c: return False,'no country'
    lid='lie_1'; lie={'id':lid,'name':name}; c.setdefault('shadow',{}).setdefault('lieutenants',{})[lid]=lie; db.put(f'countries/{country_id}', c); return True,lie
