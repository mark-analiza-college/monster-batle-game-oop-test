import random
from time import sleep


class BaseCompetitor():
  def __init__(self, name):
    self.name = name
    self.hp = 50
    self.speed = random.randint(0, 5)
    self.power = random.randint(5, 10)


  def roll_first_turn_dice(self):
    return random.randint(1, 6) + self.speed

  def get_shield_attack_damage(self):
    return random.randint(1, 20) + self.power

  def get_damage_dice(self):
    return random.randint(1, 6) + self.power


  def attack(self, defender):

    self.speak()
    sleep(2)
    sheild_damage = self.get_shield_attack_damage()
    if sheild_damage > defender.armor_rating:
      defender.hp -= self.get_damage_dice()


  def speak(self):
    print(f"My name is {self.name} and I am a {self.__class__.__name__} and I am going to bust your little ass")


  def __str__(self):
    return f"{self.__class__.__name__}: Name: {self.name}, HP: {self.hp}"

if __name__ == "__main__":
  base_competitor = BaseCompetitor("John")
  print(base_competitor)