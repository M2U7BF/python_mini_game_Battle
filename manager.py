import subprocess

class Manager :
    pass

margin = 20

def initialize_games():
    subprocess.run("clear")

def hoimi_slime_image():
    print(" "*3+"●"*3+"●"*2+" "*1)
    print(" "*2+"●"*2+"◎"*1+"●"*1+"◎"*1+"●"*2)
    print(" "*3+"●"*3+"●"*2+" "*1)
    print((" "*2+"●")*3)
    print((" "*2+"●")*3)
    print("\n"*1)

def game_info(player,enemy):
    str_player_hp = f"{player.name} HP : "
    str_enemy_hp = f"{enemy.name} HP : "
    
    for i in range(player.hp):
        str_player_hp += "]"

    for i in range(enemy.hp):
        str_enemy_hp += "]"

    print(str_player_hp)
    print(str_enemy_hp)

def battle(enemy,player):
    if enemy.hp<0 or player.hp<0:
        return

    initialize_games()
    turn = 1

    print(f"{enemy.name}が現れた\n")
    hoimi_slime_image()

    print(f"{enemy.name}はいきなり襲いかかってきた\n")

    print("-"*margin+"[< BATTLE START >]"+"-"*margin)
    print("\n"*1)

    while enemy.hp>0 and player.hp>0 :
        print("-"*margin+"> enemy turn  "+" "*margin)
        print("\n"*1)
        enemy.enemy_action(player)
        print("\n"*1)
        print("-"*margin+"> your turn  "+" "*margin)
        player.player_action(enemy)
        
        if enemy.hp<0 or player.hp<0:
            print("="*margin+"[< RESULT >]"+"="*margin)
            if enemy.hp<0:
                print(f"{player.name}は{enemy.name}を倒した!\n") 
            elif player.hp<0:
                print(f"{player.name}は力尽きた...")
                break;
            print("="*50)
        print("-"*margin+"> turn end <"+"-"*margin)
        turn += 1

        enter = input("")
        subprocess.run("clear")
        
        print(" "*margin+f"[[ turn : {turn} ]]"+" "*margin)
        print("\n"*1)
        game_info(player,enemy)
        print("\n"*2)