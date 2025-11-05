import random
from core.base_competitor import BaseCompetitor

class Player(BaseCompetitor):
  def __init__(self, name):
    super().__init__(name)
    self.speed = random.randint(5, 10)
    self.power = random.randint(5, 10)
    self.armor_rating = random.randint(5, 15)
    self.profession = random.choice(["warrior", "healer"])

    if self.profession == "healer":
      self.hp = self.hp + 10
    elif self.profession == "warrior":
      self.power = self.power + 2


  def __str__(self):
    return f"{super().__str__()}, Profession: {self.profession}, Speed: {self.speed}, Power: {self.power}, Armor Rating: {self.armor_rating}"

if __name__ == "__main__":
  player = Player("John")
  print(player)