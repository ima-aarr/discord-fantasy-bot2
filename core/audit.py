from core import db
import datetime

def log(action, actor, details):
    entry={'time': datetime.datetime.utcnow().isoformat(),'action':action,'actor':actor,'details':details}
    try: db.post('audit_logs', entry)
    except Exception as e: print('audit log err', e)
