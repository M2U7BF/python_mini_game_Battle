class UniqueCharacter(object):
    """
    行動を持つキャラクターのクラス
    """

    def __init__(self, name, ability) -> None:
        self.name = name
        self.ability = ability

        self.is_guarding = 0
        self.max_hp = ability.hp
        self.max_mp = ability.mp
