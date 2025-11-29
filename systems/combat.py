from core import db, audit
from utils.combat_engine import compute_party_power, compute_monster_power

def resolve_party_vs_monster(server_id, party_id, monster):
    party=db.get(f'worlds/{server_id}/parties/{party_id}'); return True,{'result':'victory'}
