import random
import monster_datas
import attack_defens
from monster_datas import monster_data

# 各怪物對應的戰鬥邏輯函式
monster_logic_map = {
    "白目鍋鍋獸": attack_defens.battle_logic_pot_monster,
    "自戀狂魅獸": attack_defens.battle_logic_narcissist_monster,
    "控場霸言獸": attack_defens.battle_logic_command_monster,
    "白臉黑腹獸": attack_defens.battle_logic_double_face_monster,
    "霸總龍王獸": attack_defens.battle_logic_boss_monster
}

# 勇者類別，包含等級成長邏輯
class Player:
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.atk_range = (20, 50)

    def level_up(self, level):
        self.level = level
        if level == 1:
            self.hp = 100
            self.atk_range = (20, 50)
        elif level == 2:
            self.hp = 150
            self.atk_range = (35, 65)
        elif level == 3:
            self.hp = 200
            self.atk_range = (50, 80)
        elif level == 4:
            self.hp = 250
            self.atk_range = (65, 100)

# 安全選字（避免資料是 str 而非 list）
def safe_random_choice(item):
    if isinstance(item, list):
        return random.choice(item)
    elif isinstance(item, str):
        return item
    return ""

# 單層戰鬥流程
def battle_one_floor(player, monster_name, level):
    monster = monster_data[monster_name]
    monster_hp = monster["hp"]
    monster_logic = monster_logic_map[monster_name]

    print(f"\n🗼【第 {level} 層】{monster_name} 出現了！")
    print(monster["intro"])

    # 升級勇者能力
    player.level_up(level)
    state = {}
    round_count = 1

    while player.hp > 0 and monster_hp > 0:
        print(f"\n--- 第 {round_count} 回合 ---")
        print(f"【勇者 HP】: {player.hp} / 【{monster_name} HP】: {monster_hp}")

        while True:
            player_action = input("請選擇你的行動 (attack / defense): ").strip()
            print("*"*50)
            if player_action in ["attack", "defense", "加油"]:
                break
            print("⚠️ 無效輸入，請重新輸入：attack / defense")

        # 如果怪物是只攻擊型，固定為 attack
        if "only_attack" in monster and monster["only_attack"] is True:
            monster_action = "attack"
        else:
            monster_action = random.choice(["attack", "defense"])

        player_act = random.randint(*player.atk_range)
        monster_act = random.randint(*monster["attack_range"])

        player.hp, monster_hp, p_dmg, m_dmg, last_move = monster_logic(
            player_action, monster_action, player.hp, monster_hp,
            player_act, monster_act, monster, state
        )

        # 顯示回合結果
        if p_dmg == 0 and m_dmg == 0:
            print("⚔️ 雙方僵持不下，沒有造成任何傷害。")
        else:
            print(f"【勇者】打出 {p_dmg} 點傷害，怪物打出 {m_dmg} 點傷害")

        print(f"【勇者 HP】: {player.hp} / 【{monster_name} HP】: {monster_hp}")
        if monster_hp <= 0:
            print("✅ 勇者擊敗了", monster_name)
            if monster_name == "自戀狂魅獸":
                if last_move == "defense_defense":
                        print("「不愧是我……太犯規了……」──【怪物】在陶醉中失去意識。伴隨著擠到閃光，手機緩緩飄向【勇者】手中。")
                else:
                        print("【怪物】:「不……不能讓這張臉……毀了……！」牠緩緩倒下，姿勢宛如拍封面，一道粉紅色煙霧裡閃著自拍閃光燈。手機緩緩飄向【勇者】手中。")

            elif "death_line" in monster:
                    print(safe_random_choice(monster["death_line"]))

            return True
        if player.hp <= 0:
            print("❌ 勇者倒下了……")
            return False
        round_count += 1

# 主流程：爬塔
def main_battle():
    player = Player()
    tower_monsters = ["白目鍋鍋獸", "自戀狂魅獸", "控場霸言獸", "白臉黑腹獸", "霸總龍王獸"]

    for level, monster_name in enumerate(tower_monsters, start=1):
        win = battle_one_floor(player, monster_name, level)
        if not win:
            print(f"\n💀 勇者挑戰失敗，止步第 {level} 層。")
            break
    else:
        print("\n🎉 恭喜勇者通過試煉之塔！")

if __name__ == "__main__":
    main_battle()
