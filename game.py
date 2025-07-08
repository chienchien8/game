class Monster:
    def __init__(self, name):
        data = monster_data[name]
        self.name = name
        self.hp = data["hp"]
        self.min_atk, self.max_atk = data["attack_range"]
        self.intro = data["intro"]
        self.attack_descriptions = data["attack_descriptions"]
        self.hurt_reactions = data["hurt_reactions"]
        self.death_line = data["death_line"]

class Player:
    def __init__(self, hp, attack_range):
        self.hp = hp
        self.min_atk, self.max_atk = attack_range
