import random
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin
from core.base_competitor import BaseCompetitor
from core.base_monster import BaseMonster

class Game():

  def roll_dice(self) -> BaseCompetitor:
    player_dice = self.player.roll_first_turn_dice()
    monster_dice = self.monster.roll_first_turn_dice()
    if player_dice >= monster_dice:
      return self.player
    else:
      return self.monster


  def show_menu(self):
    user_input = None
    while user_input is None or user_input not in [1, 2]:
      print("1. Play")
      print("2. Quit")
      try:
        user_input = int(input("Enter your choice: "))
        if user_input not in [1, 2]:
          print("Invalid choice. Please enter 1 or 2.")
          continue
        else:
          user_input = int(user_input)
          break
      except ValueError:
        print("Invalid choice. Please enter 1 or 2.")
        continue
    return user_input

  def create_player(self) -> Player:
    return Player("John")

  def choose_random_monster(self) -> BaseMonster:
    return random.choice([Orc("Orc-BABI-123"), Goblin("Goblin-BABI-123")])

  def battle(self, competitor1, competitor2):
     competitor1.attack(competitor2)
     print(f"{competitor1.name} attacks {competitor2.name} he has {competitor2.hp} hp left!")
     print("===================================================")
     if(competitor2.hp <= 0):
      print(f"{competitor1.name} wins!")
      return
     else:
      competitor2.attack(competitor1)
      print(f"{competitor2.name} attacks {competitor1.name} he has {competitor1.hp} hp left!")
      print("===================================================")
      if(competitor1.hp <= 0):
        print(f"{competitor2.name} wins!")
        return
      else:
        self.battle(competitor1, competitor2)
  
  def start(self):

    self.player = self.create_player()

    players_choice = self.show_menu()
    
    if players_choice == 2:
      print("Thank you for playing! Bye bye")
      return
    else:
      self.monster = self.choose_random_monster()

      first_turn_competitor = self.roll_dice()
      if first_turn_competitor == self.player:
        self.battle(self.player, self.monster)
      else:
        self.battle(self.monster, self.player)

      print("Thank you for playing!")
      return
