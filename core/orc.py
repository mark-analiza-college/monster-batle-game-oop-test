import random
from core.base_monster import BaseMonster

class Orc(BaseMonster):
  def __init__(self, name):
    super().__init__(name)
    self.type = "orc"
    self.speed = random.randint(0, 5)
    self.power = random.randint(10, 15)
    self.armor_rating = random.randint(2, 8)


if __name__ == "__main__":
  orc = Orc("Orc-BABI-123")
  print(orc)