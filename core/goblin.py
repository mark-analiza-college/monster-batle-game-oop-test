import random
from core.base_monster import BaseMonster

class Goblin(BaseMonster):
  def __init__(self, name):
    super().__init__(name)
    self.hp = 20
    self.type = "goblin"
    self.speed = random.randint(5, 10)
    self.power = random.randint(5, 10)
    self.armor_rating = 1

    
  def __str__(self):
    return f"{super().__str__()}, Speed: {self.speed}, Power: {self.power}, Armor Rating: {self.armor_rating}"

if __name__ == "__main__":
  goblin = Goblin("Goblin-BABI-123")
  print(goblin)
  goblin.speak()

