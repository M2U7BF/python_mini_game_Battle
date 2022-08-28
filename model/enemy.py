import random
import math

from Action import Action

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

    def enemy_action(self, player):
        dict1 = {
            "attack" : f"{self.name}の攻撃\n",
            "guard" : f"{self.name}は攻撃に備えた\n",
            "recover" : f"{self.name}は回復をした\n",
            "flee" : f"{self.name}は逃げ出した\n",
            "listening" : f"{self.name}は様子をうかがっている"
        }

        dict2 = {
            "attacked" : "",
            "guarded" : f"{self.name}は堅く身を守っている\n",
            "recovered" : "",
            "fled" : "逃げ切れた...\n",
            "fled_missed" : "しかし、回り込まれた\n"
        }

        action_num = random.randrange(self.quietness)

        actions = Action(dict1,dict2)

        if action_num == 0:
            actions.attack(self,player)
        elif action_num == 1:
            actions.recovery(self)
        else:
            actions.listening()
