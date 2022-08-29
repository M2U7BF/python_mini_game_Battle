import math
import subprocess


class Manager:
    battle_end = 0

    def __init__(self) -> None:
        self.battle_end = 0


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


def game_info(player, enemy):
    str_player_hp = f"HP : {player.ability.hp}/{player.ability.max_hp}"
    str_player_mp = f"MP : {player.ability.mp}/{player.ability.max_mp}"
    str_enemy_hp = f"HP : {enemy.ability.hp}/{enemy.ability.max_hp}"
    str_enemy_mp = f"MP : {enemy.ability.mp}/{enemy.ability.max_mp}"

    for i in range(math.ceil(player.ability.hp/10)):
        str_player_hp += "]"
    for i in range(math.ceil(player.ability.mp/10)):
        str_player_mp += "]"

    for i in range(math.ceil(enemy.ability.hp/10)):
        str_enemy_hp += "]"
    for i in range(math.ceil(enemy.ability.mp/10)):
        str_enemy_mp += "]"

    print(f"{player.name}\n")
    print(str_player_hp)
    print(str_player_mp)
    print("\n")
    print(f"{enemy.name}\n")
    print(str_enemy_hp)
    print(str_enemy_mp)


def turn_end_process(enemy, player):
    player.is_guarding = 0
    enemy.is_guarding = 0

def battle_result(enemy, player):
    exp_earned = enemy.ability.power + enemy.ability.max_hp + enemy.ability.max_mp
    print(f"{player.name}の獲得経験値 : {exp_earned}")
    player.exp += exp_earned

def battle(enemy, player):
    manager = Manager()

    if enemy.ability.hp < 0 or player.ability.hp < 0:
        return

    initialize_games()
    turn = 1

    print(f"{enemy.name}が現れた\n")
    hoimi_slime_image()

    print(f"{enemy.name}はいきなり襲いかかってきた\n")

    print("-"*margin+"[< BATTLE START >]"+"-"*margin)
    print("\n"*1)
    game_info(player, enemy)
    print("\n"*1)

    while enemy.ability.hp > 0 and player.ability.hp > 0:
        print("-"*margin+"> enemy turn  "+" "*margin)
        print("\n"*1)
        enemy.enemy_action(player)
        print("\n"*1)

        turn_end_process(enemy, player)

        print("-"*margin+"> your turn  "+" "*margin)
        player.player_action(enemy,manager)

        if enemy.ability.hp < 0 or player.ability.hp < 0:
            print("="*margin+"[< RESULT >]"+"="*margin)
            if enemy.ability.hp <= 0:
                print(f"{player.name}は{enemy.name}を倒した!\n")
                print("\n")
                battle_result(enemy, player)
                manager.battle_end = 1
            elif player.ability.hp <= 0:
                print(f"{player.name}は力尽きた...")
                manager.battle_end = 1
            print("="*50)

        if manager.battle_end == 1:
            break

        print("-"*margin+"> turn end <"+"-"*margin)
        turn += 1

        enter = input("")
        subprocess.run("clear")

        print(" "*margin+f"[[ turn : {turn} ]]"+" "*margin)
        hoimi_slime_image()
        game_info(player, enemy)
        print("\n"*2)

def initial_settings():
    name = input("名前は何と言う? : ")