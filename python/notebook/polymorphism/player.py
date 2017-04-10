from character import Character

class Player(Character):
    def get_damage(self, attack_power, attack_kind):
        self.hp -= attack_power # 오버라이딩 (재정의)
 