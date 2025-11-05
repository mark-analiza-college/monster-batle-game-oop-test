
import random
from core.base_competitor import BaseCompetitor

class BaseMonster(BaseCompetitor):
  def __init__(self, name):
    super().__init__(name)
    self.hp = 50
    self.speed = random.randint(0, 5)
    self.power = random.randint(5, 10)
    self.weapon = random.choice(["knife", "axe", "sword"])
    self.armor_rating = 1

  def get_damage_dice(self):
    weapon_damage = 0
    if self.weapon == "axe":
      weapon_damage = 1.5
    elif self.weapon == "sword":
      weapon_damage = 1
    elif self.weapon == "knife":
      weapon_damage = 0.5
    return (random.randint(1, 6) + self.power) * weapon_damage

  def __str__(self):
    return f"{super().__str__()}, Speed: {self.speed}, Power: {self.power}"

if __name__ == "__main__":
  base_monster = BaseMonster("John")
  print(base_monster)
  print(base_monster.get_damage_dice())