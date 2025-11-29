# utils/combat_engine.py

import random
import math

# ---------------------------------------------------
# 個人の戦闘力
# ---------------------------------------------------
def compute_player_power(stats: dict) -> float:
    return (
        stats.get("strength", 1) * 2 +
        stats.get("agility", 1) * 1.2 +
        stats.get("magic", 1) * 1.5 +
        stats.get("vitality", 1) * 1.3
    )


# ---------------------------------------------------
# パーティ全体の戦闘力（battle_cog が必ず要求する）
# ---------------------------------------------------
def compute_party_power(party: list) -> float:
    """
    party = [
        {
            "name": "...",
            "stats": {...},
            "hp": int
        },
        ...
    ]
    """
    power = 0
    for member in party:
        power += compute_player_power(member.get("stats", {}))

    # パーティ補正（人数が多いほどボーナス）
    party_bonus = 1 + (len(party) - 1) * 0.15
    return power * party_bonus


# ---------------------------------------------------
# モンスターの戦闘力
# ---------------------------------------------------
def compute_monster_power(level: int) -> int:
    base = 12 + level * 5
    variance = random.randint(-4, 4)
    return max(1, base + variance)


# ---------------------------------------------------
# 1体 vs 1体（プレイヤー戦）
# ---------------------------------------------------
def simulate_battle(player: dict, monster: dict) -> dict:
    result = {
        "turns": [],
        "player_hp": player["hp"],
        "monster_hp": monster["hp"],
        "winner": None
    }

    player_atk = compute_player_power(player["stats"])
    monster_atk = compute_monster_power(monster["level"])

    turn = 1
    while result["player_hp"] > 0 and result["monster_hp"] > 0:

        # Player attack
        dmg_to_monster = max(1, int(player_atk * random.uniform(0.6, 1.3)))
        result["monster_hp"] -= dmg_to_monster
        result["turns"].append(
            f"Turn {turn}: {player['name']} が {monster['name']} に {dmg_to_monster} ダメージ！"
        )
        if result["monster_hp"] <= 0:
            result["winner"] = "player"
            break

        # Monster attack
        dmg_to_player = max(1, int(monster_atk * random.uniform(0.5, 1.2)))
        result["player_hp"] -= dmg_to_player
        result["turns"].append(
            f"Turn {turn}: {monster['name']} の攻撃！ {player['name']} は {dmg_to_player} ダメージ！"
        )
        if result["player_hp"] <= 0:
            result["winner"] = "monster"
            break

        turn += 1

    return result


# ---------------------------------------------------
# パーティ VS モンスターの戦闘
# ---------------------------------------------------
def simulate_party_battle(party: list, monster: dict) -> dict:
    """
    party = [ { "name": str, "hp": int, "stats": {...} }, ... ]
    """
    result = {
        "turns": [],
        "party_hp": sum(member["hp"] for member in party),
        "monster_hp": monster["hp"],
        "winner": None
    }

    party_power = compute_party_power(party)
    monster_power = compute_monster_power(monster["level"])

    turn = 1
    while result["party_hp"] > 0 and result["monster_hp"] > 0:

        # Party attack
        dmg_to_monster = max(1, int(party_power * random.uniform(0.3, 0.7)))
        result["monster_hp"] -= dmg_to_monster
        result["turns"].append(
            f"Turn {turn}: パーティが {monster['name']} に {dmg_to_monster} ダメージ！"
        )
        if result["monster_hp"] <= 0:
            result["winner"] = "party"
            break

        # Monster attack
        dmg_to_party = max(1, int(monster_power * random.uniform(0.4, 1.0)))
        result["party_hp"] -= dmg_to_party
        result["turns"].append(
            f"Turn {turn}: {monster['name']} の反撃！ パーティに {dmg_to_party} ダメージ！"
        )
        if result["party_hp"] <= 0:
            result["winner"] = "monster"
            break

        turn += 1

    return result


# ---------------------------------------------------
# 報酬（個人 & パーティ共通）
# ---------------------------------------------------
def compute_battle_rewards(monster: dict) -> dict:
    base_gold = 25 + monster["level"] * 6
    base_exp = 20 + monster["level"] * 4

    return {
        "gold": int(base_gold * random.uniform(0.8, 1.3)),
        "exp": int(base_exp * random.uniform(0.8, 1.3)),
    }
