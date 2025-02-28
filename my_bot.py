from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType
import time
import random

BOT_NAME = "SUTTER LIDT" # Change this to your bot's name

class Bot:
  @classmethod
  def get_name_class(cls, path):
    return BOT_NAME

  def get_name(self):
      return BOT_NAME

  def act(self, obs: Observation):
    # Your code here
    bb = obs.get_my_player_info().stack / obs.big_blind

    #print(bb)
    myhand = obs.my_hand

    default = 1
    if obs.legal_actions.__contains__(0):
      default = 0


    if (bb >= 50):
      range = Range("KK+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
      
    if (bb >= 35):
      range = Range("QQ+,AKs,AKo+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
    
    if (bb >= 30):
      range = Range("JJ+, AQs+, AKo")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
    
    if (bb >= 25):
      range = Range("TT+, AJs+, AQo+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
    
    if (bb >= 20):
      range = Range("99+, ATs+, AJo+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
      
    if (bb >= 17):
      range = Range("88+, A8s+, A4s-A5s, KQs, ATo+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
      
    if (bb >= 15):
      range = Range("66+, A2s+, KJs+, ATo+, KQo")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default
      
    if (bb >= 12):
      range = Range("44+, A2s+, KTs+, A8o+, KJo+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default

    if (bb >= 10):
      range = Range("22+, A2s+, K7s+, QJs, A8o+, KTo+")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default

    if (bb >= 8):
      range = Range("22+, A2s+, K4s+, Q8s+, J9s+, T9s, A8o+, K9o+, QJo")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default

    if (bb < 8):
      range = Range("22+, A2s+, K4s+, Q8s+, J9s+, T9s, A8o+, K9o+, QJo")
      if range.is_hand_in_range(myhand): 
        return obs.get_max_raise()
      else:
        return default

    else:  
      return default
