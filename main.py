import random
from player import Player
from enemy import Enemy
from manager import *
import subprocess

player = Player("computer",100,10)

enemy = Enemy("ホイミスライム Lv.5",30,10)
enemy1 = Enemy("ホイミスライム Lv.20",80,16)
enemy2 = Enemy("ホイミスライム Lv.50",100,30)
enemy3 = Enemy("くさった死体",30,20)

battle(enemy,player)
battle(enemy1,player)
battle(enemy2,player)
battle(enemy3,player)

# subprocess.run("clear")

# print("ホイミスライム")
# print("メタルスライム")
# print("くさった死体")
# print("マドハンド")
# print("ゴーレム")