from pickle import FALSE, TRUE
import random
from Action import Action

from model.unique_charcter import UniqueCharacter


class Player(UniqueCharacter):
    def __init__(self, name, ability) -> None:
        super().__init__(name, ability)
        self.exp = 0

    def player_action(self, enemy, manager):
        dict1 = {
            "attack" : self.name+"の攻撃\n",
            "guard" : self.name+"は攻撃に備えた\n",
            "recover" : self.name+"は回復の呪文を唱えた\n",
            "flee" : self.name+"は逃げ出した\n"
        }

        dict2 = {
            "attacked" : "",
            "guarded" : f"{self.name}は堅く身を守っている\n",
            "recovered" : "",
            "fled" : "逃げ切れた...\n",
            "fled_missed" : "しかし、回り込まれた\n"
        }

        actions = Action(dict1,dict2)

        action = input("1.攻撃 2.防御 3.回復 4.逃げる\n行動の選択 : ")
        # action = action.strip() # 空白文字のみの入力は無視する

        print("\n")
        if action == '' or action == "1":
            actions.attack(self,enemy)
        elif action == "2":
            actions.guard(self)
        elif action == "3":
            actions.recovery(self)
        elif action == "4":
            print(dict1["flee"])
            self.player_flee(manager)

    def player_flee(self,manager):
        value = random.randrange(3)
        if value == 0:
            print("逃げ切れた...\n")
            enter = input("")
            manager.battle_end = 1
        else:
            print("しかし、回り込まれた\n")
