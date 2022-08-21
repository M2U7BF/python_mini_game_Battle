import random

class Player:
    def __init__(self,name,hp,pw) -> None:
        self.name  = name
        self.hp = hp
        self.pw = pw
        pass

    def player_action(self,enemy) :
        name = "computer"
        strs = [name+"の攻撃\n",name+"は攻撃に備えた\n",name+"は回復の呪文を唱えた\n",name+"は逃げ出した\n"]
        action = input("1.攻撃 2.防御 3.回復 4.逃げる\n行動の選択 : ")
        # action = action.strip() # 空白文字のみの入力は無視する
        
        print("\n")
        if action=='' or action == "1":
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
            self.player_flee()

    def player_attack(self,enemy):
        damage = random.randrange(self.pw)
        print(f"相手に{damage}のダメージ\n")
        enemy.hp -= damage

    def player_guard(self):
        print("computerは堅く身を守っている\n")

    def player_recovery(self):
        value = random.randrange(10)
        print(f"{value}の回復\n")
        self.hp += value

    def player_flee(self):
        value = random.randrange(2)
        if value==0 :
            print("逃げ切れた\n")
        else:
            print("しかし、回り込まれた\n")