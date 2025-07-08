import random
import monster_datas

#白目嘓嘓獸
def battle_logic_pot_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act

    elif player_action == "attack" and monster_action == "defense":
        act = random.choice(data["attack_defense"])
        print(act)
        if "無辜之臉" in act:
            monster_hp -= player_act // 2
        elif "被甩回來" in act:
            player_hp -= player_act // 2
            monster_hp -= player_act // 2

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        player_hp -= monster_act // 2

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))

    return player_hp, monster_hp

# 自戀狂魅獸
def battle_logic_narcissist_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act

    elif player_action == "attack" and monster_action == "defense":
        print(random.choice(data["attack_defense"]))
        player_hp -= player_act // 2

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        player_hp -= 0

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))
        monster_hp = 0
        print(random.choice(data["death_line"]))

    return player_hp, monster_hp

# 控場霸言獸
def battle_logic_command_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act

    elif player_action == "attack" and monster_action == "defense":
        act = random.choice(data["attack_defense"])
        print(act)
        # 攻擊無效
        pass

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))

    return player_hp, monster_hp

# 白臉黑腹獸
def battle_logic_double_face_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    # 初始化防禦次數與是否進入「弱點暴露狀態」
    state.setdefault("defend_count", 0)
    state.setdefault("vulnerable", False)

    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        # 如果先前已防禦3次，進入「弱點暴露狀態」，玩家這次攻擊必殺
        if state["vulnerable"]:
            print("【勇者】抓準破綻，一擊斬斷雙面獸的虛偽面具！")
            monster_hp = 0
        else:
            monster_hp -= player_act
        state["vulnerable"] = False  # 用完就重置

    elif player_action == "attack" and monster_action == "defense":
        print(random.choice(data["attack_defense"]))
        if state["vulnerable"]:
            print("【勇者】抓準時機，斬斷防禦！")
            monster_hp = 0
        else:
            monster_hp -= player_act // 2
        state["vulnerable"] = False

    elif player_action == "defense" and monster_action == "attack":
        if state["defend_count"] < 3:
            print(data["defense_attack"][state["defend_count"]])
            state["defend_count"] += 1
        if state["defend_count"] >= 3:
            print("【勇者】看穿了雙面獸的虛偽！下一次攻擊將擊潰牠！")
            state["vulnerable"] = True

    elif player_action == "defense" and monster_action == "defense":
        print(random.choice(data["defense_defense"]))
        # 不重置 vulnerable 狀態

    return player_hp, monster_hp


#霸總龍王獸
def battle_logic_boss_monster(player_action, monster_action, player_hp, monster_hp, player_act, monster_act, data, state):
    if player_action == "attack" and monster_action == "attack":
        print(random.choice(data["attack_attack"]))
        player_hp -= monster_act
        monster_hp -= player_act

    elif player_action == "defense" and monster_action == "attack":
        print(random.choice(data["defense_attack"]))
        player_hp -= monster_act // 2

    elif player_action == "加油":
        print("【勇者】鼓起勇氣，內心充滿力量！")
        monster_act = 0

    return player_hp, monster_hp