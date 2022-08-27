import random
import math

from .unique_charcter import UniqueCharacter


class Enemy(UniqueCharacter):
    quietness = 5

    def __init__(self, name, ability) -> None:
        super().__init__(name, ability)

    def enemy_attack(self, player):
        damage = random.randrange(self.ability.power)
        if player.is_guarding == 1:
            damage = math.ceil(damage/3)
        print(f"{damage}のダメージ\n")
        player.ability.hp -= damage

    def enemy_recovery(self):
        if self.ability.magical_power == 0:
            print(f"{self.name}は回復ができない\n")
        else:
            value = random.randrange(self.ability.magical_power)
            print(f"{value}回復\n")

            if self.ability.hp+value > self.max_hp:
                self.ability.hp = self.max_hp
            else:
                self.ability.hp += value

    def enemy_action(self, player):
        strs = [self.name+"の攻撃\n", self.name +
                "は回復をした\n", self.name+"は様子をうかがっている\n"]

        action_num = random.randrange(self.quietness)

        if action_num == 0:
            print(strs[0])
            self.enemy_attack(player)
        elif action_num == 1:
            print(strs[1])
            self.enemy_recovery()
        else:
            print(strs[2])
