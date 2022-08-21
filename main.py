import random
from player import Player
from enemy import Enemy

player_hp = 100

def game_info(player_hp,enemy_hp):
    str_player_hp = "player HP : "
    str_enemy_hp = "enemy HP : "
    
    for i in range(player_hp):
        str_player_hp += "]"

    for i in range(enemy_hp):
        str_enemy_hp += "]"

    print(str_player_hp)
    print(str_enemy_hp)

##############################################

margin = 20

player = Player("computer",100,10)
enemy = Enemy("ホイミスライム",30,10)

print(f"{enemy.name}が現れた\n")
print(f"{enemy.name}はいきなり襲いかかってきた\n")

print("-"*margin+"[< BATTLE START >]"+"-"*margin)
print("\n"*1)

while enemy.hp>0 and player.hp>0 :
    print("-"*margin+"[ enemy turn ]"+"-"*margin)
    print("\n"*1)
    enemy.enemy_action(player)
    print("\n"*1)
    print("-"*margin+"[ your turn ]"+"-"*margin)
    print("\n"*1)
    game_info(player.hp,enemy.hp)
    print("\n"*2)
    player.player_action(enemy)
    
    if enemy.hp<0 or player.hp<0:
        print("-"*margin+"[< RESULT >]"+"-"*margin)
        if enemy.hp<0:
            print(f"{player.name}は{enemy.name}を倒した!\n") 
        elif player.hp<0:
            print(f"{player.name}は力尽きた...")
    print("-"*margin+"> turn end <"+"-"*margin)
    print("\n"*5)

# print("ホイミスライム")
# print("メタルスライム")
# print("くさった死体")
# print("マドハンド")
# print("ゴーレム")