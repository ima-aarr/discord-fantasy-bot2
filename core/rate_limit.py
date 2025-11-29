import time
from core import db
from config import RATE_LIMIT_USER
def check_and_bump_user(user_id: str, window: int = 60, limit: int = None):
    limit = limit or RATE_LIMIT_USER
    bucket = str(int(time.time()//window))
    path = f"rate_limits/users/{user_id}/{bucket}"
    cur = db.get(path) or 0
    if cur >= limit: return False
    try: db.put(path, cur+1)
    except Exception as e:
        print('rate limit db error', e); return False
    return True
