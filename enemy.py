import random

class Enemy:
    def __init__(self,name,hp,pw) -> None:
        self.name = name
        self.hp = hp
        self.pw = pw
        pass

    def enemy_attack(self,player):
        damage = random.randrange(self.pw)
        print(f"{damage}のダメージ\n")
        player.hp -= damage

    def enemy_recovery(self):
        value = random.randrange(10)
        print(f"{value}回復\n")
        self.hp += value

    def enemy_action(self,player):
        strs = [self.name+"の攻撃\n",self.name+"は回復をした\n",self.name+"は様子をうかがっている\n"]

        action_num = random.randrange(5)
        if action_num == 0:
            print(strs[0])
            self.enemy_attack(player)
        elif action_num == 1:
            print(strs[1])
            self.enemy_recovery()
        else:
            print(strs[2])