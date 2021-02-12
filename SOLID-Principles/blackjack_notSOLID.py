# Implementation of card and shoe for a Black Jack game
# Goal is to analyze the SOLID principles:
# Single Responsibility, Open/Close, Liskov Substitution, Interface Segregation , Dependency Inversion
# Code inspired in Steven Lott's course.

import random

"""
This class has some problems with it,
it both implements a deck of cards, and the cards themselves
It also implements the point counting, which is particular to BlackJack, so 
we wouldn't be able to reuse this class if we wanted to.
"""
class Card():
    def __init__(self):
        self.cards = [(rank, suit) # A list of tuples, which represents a single card
            for rank in range(1, 14) # range doesn't include the last number!
            for suit in 'HSCD'] # Hearts, Spades, Clubs, Diamonds
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def points(self, card):
        rank, suit = card
        if rank == 1:
            return (1,11)
        elif 2 <= rank < 11:
            return (rank,rank)
        else:
            return (10,10)

class Shoe(Card):
    def __init__(self, n):
        super().__init__()
        self.shoe = []
        for _ in range(n):
            self.shoe.extend(self.cards)
        random.shuffle(self.shoe)

    def shuffle_burn(self, n=100):
        random.shuffle(self.shoe)
        self.shoe = self.shoe[n:]

    def deal():
        return self.shoe.pop()

"""
Articulating the problems:
- Mixed responsibilities: card, deck, points
- Missing responsibilities: total points to the black jack game?
- Limit reuse: can't use for cribbage for example
- Not substitutable: can't use a shoe in the place of a card
- Haphazard interface: (?) should be iterable.

Goals for our solid design: prevent problems, and differentiate changes that would be relevant.
"""


