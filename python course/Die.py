import random
class Die:
    """A Die"""
    def __init__(self, sides=6):
        """Creates a new standard die
        Keyword aguments:
        sides(int) -- number of die sides."""
        self._sides = sides
        self._rolls = []
    # add a roll() method
    @property
    def rolls(self):
        "history of rolls"
        return self._rolls
    def roll(self):
        """returns a value between 1 and the number of die sides."""
        return(random.randint(1, self.sides))