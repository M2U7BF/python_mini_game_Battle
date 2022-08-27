import random


class Action(object):
    """
    行動を定義するクラス
    """
    def __init__(self,before_action_massage,after_action_message) -> None:
        self.before_action_massage = before_action_massage
        self.after_action_message = after_action_message

    def attack(self, subject, enemy):
        print(self.before_action_massage["attack"])
        damage = random.randrange(subject.ability.power)
        print(f"相手に{damage}のダメージ\n")
        enemy.ability.hp -= damage

    def guard(self, subject):
        print(self.before_action_massage["guard"])
        subject.is_guarding = 1
        print(self.after_action_message["guard"])

    def recovery(self,subject):
        print(self.before_action_massage.recover)
        if subject.ability.magical_power == 0:
            print(f"{subject.name}は回復ができない\n")
        else:
            value = random.randrange(subject.ability.magical_power)
            print(f"{value}回復\n")

            if subject.ability.hp+value > subject.max_hp:
                subject.ability.hp = subject.max_hp
            else:
                subject.ability.hp += value

    def listening(self):
        print(self.before_action_massage["listening"])