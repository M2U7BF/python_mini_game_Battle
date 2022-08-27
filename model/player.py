from pickle import FALSE, TRUE
import random

from model.unique_charcter import UniqueCharacter


class Player(UniqueCharacter):
    def __init__(self, name, ability) -> None:
        super().__init__(name, ability)

    def player_action(self, enemy, manager):
        strs = [self.name+"の攻撃\n", self.name+"は攻撃に備えた\n",
                self.name+"は回復の呪文を唱えた\n", self.name+"は逃げ出した\n"]
        action = input("1.攻撃 2.防御 3.回復 4.逃げる\n行動の選択 : ")
        # action = action.strip() # 空白文字のみの入力は無視する

        print("\n")
        if action == '' or action == "1":
            print(strs[0])
            self.player_attack(enemy)
        elif action == "2":
            print(strs[1])
            self.player_guard()
        elif action == "3":
            print(strs[2])
            self.player_recovery()
        elif action == "4":
            print(strs[3])
            self.player_flee(manager)

    def player_attack(self, enemy):
        damage = random.randrange(self.ability.power)
        print(f"相手に{damage}のダメージ\n")
        enemy.ability.hp -= damage

    def player_guard(self):
        self.is_guarding = 1
        print(f"{self.name}は堅く身を守っている\n")

    def player_recovery(self):
        value = random.randrange(10)
        print(f"{value}の回復\n")
        if self.ability.hp+value > self.max_hp:
            self.ability.hp = self.max_hp
        else:
            self.ability.hp += value

    def player_flee(self,manager):
        value = random.randrange(3)
        if value == 0:
            print("逃げ切れた...\n")
            enter = input("")
            manager.battle_end = 1
        else:
            print("しかし、回り込まれた\n")
