import random

# 白目嘓嘓獸

def battle_logic_pot_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    player_dmg = 0
    monster_dmg = 0

    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        monster_hp -= player_act
        player_hp -= monster_act
        player_dmg = player_act
        monster_dmg = monster_act

    elif player_action == "attack" and monster_action == "defense":
        act = random.choice(data["attack_defense"])
        print(act)
        if "無辜之臉" in act:
            dmg = player_act // 2
            monster_hp -= dmg
            player_dmg = dmg
        elif "被甩回來" in act:
            dmg = player_act // 2
            player_hp -= dmg
            monster_hp -= dmg
            player_dmg = dmg
            monster_dmg = dmg

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        dmg = 0
        player_hp -= dmg
        monster_dmg = dmg

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))

    return player_hp, monster_hp, player_dmg, monster_dmg, None

# 自戀狂魅獸

def battle_logic_narcissist_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    player_dmg = 0
    monster_dmg = 0
    last_move = f"{player_action}_{monster_action}"

    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act
        player_dmg = player_act
        monster_dmg = monster_act

    elif player_action == "attack" and monster_action == "defense":
        print(random.choice(data["attack_defense"]))
        dmg = player_act // 2
        player_hp -= dmg
        monster_dmg = dmg

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        monster_dmg = 0  # 防禦成功無傷害

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))
        player_dmg = 999
        monster_hp = 0

    return player_hp, monster_hp, player_dmg, monster_dmg, last_move

# 控場霸言獸

def battle_logic_command_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    player_dmg = 0
    monster_dmg = 0

    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act
        player_dmg = player_act
        monster_dmg = monster_act

    elif player_action == "attack" and monster_action == "defense":
        act = random.choice(data["attack_defense"])
        print(act)
        # 攻擊無效，無傷害

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        dmg = 0
        player_hp -= dmg
        monster_dmg = dmg

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))

    return player_hp, monster_hp, player_dmg, monster_dmg, None

# 白臉黑腹獸
def battle_logic_double_face_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    player_dmg = 0
    monster_dmg = 0

    state.setdefault("defend_count", 0)
    state.setdefault("vulnerable", False)

    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_dmg = monster_act
        if state["vulnerable"]:
            print("【勇者】抓準破綻，一擊斬斷雙面獸的虛偽面具！")
            monster_hp = 0
            player_dmg = 999
        else:
            monster_hp -= player_act
            player_dmg = player_act
        state["vulnerable"] = False

    elif player_action == "attack" and monster_action == "defense":
        if state["vulnerable"]:
            print("【勇者】抓準時機，斬斷防禦！")
            monster_hp = 0
            player_dmg = 999
        else:
            print(random.choice(data["attack_defense"]))
            dmg = player_act // 2
            monster_hp -= dmg
            player_dmg = dmg
        state["vulnerable"] = False

    elif player_action == "defense":
        # 玩家防禦計數及提示
        if state["defend_count"] < 3:
            print(data["defense_attack"][state["defend_count"]])
            state["defend_count"] += 1
            if state["defend_count"] == 3:
                print("【勇者】看穿了雙面獸的虛偽！下一次攻擊將擊潰牠！")
                state["vulnerable"] = True
        else:
            print(data["defense_defense"])

        # 玩家防禦，不受怪物攻擊傷害
        monster_dmg = 0

    return player_hp, monster_hp, player_dmg, monster_dmg, None

# 霸總龍王獸

def battle_logic_boss_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    player_dmg = 0
    monster_dmg = 0
    if monster_action == "defense":
        monster_action = "attack"

    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act
        player_dmg = player_act
        monster_dmg = monster_act

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        dmg = monster_act // 2
        player_hp -= dmg
        monster_dmg = dmg

    elif player_action == "加油":
        print("【勇者】鼓起勇氣，內心充滿力量！")
        monster_hp = 0
        player_dmg = 99999
        monster_dmg = 0

    return player_hp, monster_hp, player_dmg, monster_dmg, None