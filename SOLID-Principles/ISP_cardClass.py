# Implementation of the Card class using the Interface Segregation Principle.

import random

# Here we're separating the classes into Card class, and a Black Jack Card class
# The interface segregation principle says that the client of an interface
# should not have to deal with methods it doesn't need
# if we kept the classes together, clients of Card, might not use the Hard()
# and Soft() methods.

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class BlackJackCard(Card):
    def __init__(self, *args):
        super().__init__(*args)
        self._hard = self.rank if self.rank <= 10 else 10
        self._soft = 11 if self.rank == 1 else self.rank if self.rank <= 10 else 10

    def Hard(self):
        return self._hard

    def Soft(self):
        return self._soft
           
class Deck:
    def __init__(self, CardType):
        self.deck = [CardType(rank, suit) 
            for rank in range(1, 14) 
            for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]]
        random.shuffle(self.deck)
    
    def Deal(self):
        return self.deck.pop()


d1 = Deck(BlackJackCard)
#card = d1.Deal()

#print(card)
#print(card.Hard())
#print(card.Soft())

print(len(d1.deck))

for card in d1.deck:
    print(card, "Soft Value=", card.Soft(), "Hard Value=", card.Hard())