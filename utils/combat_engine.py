# utils/combat_engine.py

import random
import math

# -----------------------------
# モンスターの強さを計算
# -----------------------------
def compute_monster_power(level: int) -> int:
    base = 10 + level * 4
    variance = random.randint(-3, 3)
    return max(1, base + variance)

# -----------------------------
# プレイヤーの戦闘力計算
# -----------------------------
def compute_player_power(stats: dict) -> int:
    return (
        stats.get("strength", 1) * 2 +
        stats.get("agility", 1) +
        stats.get("magic", 1) * 1.5 +
        stats.get("vitality", 1) * 1.2
    )

# -----------------------------
# 戦闘処理（高度AIバトル）
# -----------------------------
def simulate_battle(player: dict, monster: dict) -> dict:
    result = {
        "turns": [],
        "winner": None,
        "player_hp": player["hp"],
        "monster_hp": monster["hp"]
    }

    player_attack = compute_player_power(player["stats"])
    monster_attack = compute_monster_power(monster["level"])

    turn = 1
    while result["player_hp"] > 0 and result["monster_hp"] > 0:
        # プレイヤー攻撃
        dmg_to_mon = max(1, int(player_attack * random.uniform(0.6, 1.2)))
        result["monster_hp"] -= dmg_to_mon

        result["turns"].append(f"Turn {turn}: {player['name']} は {monster['name']} に {dmg_to_mon} のダメージ！")

        if result["monster_hp"] <= 0:
            result["winner"] = "player"
            break

        # モンスター反撃
        dmg_to_player = max(1, int(monster_attack * random.uniform(0.4, 1.1)))
        result["player_hp"] -= dmg_to_player

        result["turns"].append(f"Turn {turn}: {monster['name']} の攻撃！ {player['name']} は {dmg_to_player} のダメージ！")

        if result["player_hp"] <= 0:
            result["winner"] = "monster"
            break

        turn += 1

    return result

# -----------------------------
# 報酬計算
# -----------------------------
def compute_battle_rewards(monster: dict) -> dict:
    base_gold = 20 + monster["level"] * 5
    base_exp = 15 + monster["level"] * 3

    return {
        "gold": int(base_gold * random.uniform(0.8, 1.2)),
        "exp": int(base_exp * random.uniform(0.8, 1.2))
    }
