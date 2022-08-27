class AbilityScore(object):
    """
    Characterの能力値を定義
    """
    def __init__(self, hp, mp=0, magical_power=0, power=0, intelligence=0, defensive_strength=0, speed=0) -> None:
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp

        self.magical_power =magical_power
        self.power = power
        self.intelligence = intelligence
        self.defensive_strength=defensive_strength
        self.speed=speed
