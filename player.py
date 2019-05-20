import calc as clc
import deck as dk

class Player:
  def __init__(self):
    self._hand = []          # list of cards
    self._brain = clc.Calc()  # used to eval hand value

  def receive(self, card):
    self._hand.extend(card)
    self._brain.add_cards(card)

  def get_hand(self):
    return self._hand

  def put_back_hand(self):
    putback = self._hand.copy()
    self._hand = []
    self._brain.clear()
    return putback

  def look_at_table(self, cards):
    self._brain.add_cards(cards)

  def best_hand(self):
    return self._brain.best_hand()

  def get_rank(self):
    return self._brain.get_rank()

  def get_rank_as_string(self):
    return str(self._brain)

# Dealer class, is also a player
class Dealer(Player):
  # Initialize
  def __init__(self):
    super().__init__()
    self.__deck = dk.Deck()
    self.__burned = []

  def deal(self, n):
    return self.__deck.remove(n)

  def burn(self):
    self.__burned.extend(self.__deck.remove(1))

  def retrieve_cards(self, cards):
    self.__deck.add(self.__burned)
    self.__burned = []
    self.__deck.add(cards)

