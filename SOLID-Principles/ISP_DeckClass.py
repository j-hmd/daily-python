# Moving on to segregating the interface of deck and show classes
# here, the principle suggests that we should wrap the class rather than
# extending it, but in Python sometimes makes more sense to extend the class

import random

# The DeckList class inherits from the Python build in class list
class DeckList(list):
    # Here we already have the methods: pop, insert
    # which seem to be all we need to implement this class
    pass

# And if we want to build a cribbage deck based on this class we do so:
class CribbageDeck(DeckList):
    def Cut(self, depth):
        reveal = self.pop(depth)
        self.insert(0, reveal)


# This is easy to separate the making of different cards for different games
def card_factory(rank, suit):
    return BlackjackCard(rank, suit)

# More on ISP: Lott says that the ISP suggests separating the building, 
# modifying, retrieving, etc, of a particular object to another class
# so the individual parts don't influence the others by their change.

# Moving on, we analyze the deck and shoe classes, they have a lot in common,
# but Lott suggests that because the shoe has different functionality of 
# burning, this would suggest another class with shared functionality
def deck_builder(card_factory, n=1):
    return [card_factory(rank, suit) 
        for rank in range(1,14)
            for suit in ("Hearts", "Spades", "Clubs", "Diamonds")
                for _ in range(n)]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class BlackjackCard(Card):
    def __init__(self, *args):
        super().__init__(*args)
        self._hard = self.rank if self.rank <=10 else 10
        self._soft = 11 if self.rank == 1 else self.rank if self.rank <= 10 else 10
    
    def hard(self):
        return self._hard

    def soft(self):
        return self._soft

from collections.abc import MutableSequence # whose simplest example would be a list

# Then we get to the question of if we should wrap or extend a class
# we could've written the Deck class as wrapping the list build-int class
# we're not inheriting from the List class anymore, we're just exposing a limited
# interface from the list of cards.
class DeckWrapper:
    def __init__(self, cards: MutableSequence):
        self.cards = cards

    def __iter__(self):
        return iter(self.cards)
    
    def __getitem__(self, slice_or_index):
        return self.cards[slice_or_index]

    def __setitem__(self, slice_or_index, value):
        self.cards[slice_or_index] = value

    def __len__(self):
        return len(self.cards)

# Lott is saying that in python wrapping is not the best because we don't have static type checking?
# Then to implement the deck class, we're adding the burn method, but we didn't implement the __delitem__
# in the class DeckWrapper, which exposes one limitation of wrapping: we don't know how many methods in advance we will
# need to expose for a particular purpose
class Shoe1(DeckWrapper):
    def ShuffleBurn(self):
        random.shuffle(self)
        del self[-100:]

class Shoe2(DeckWrapper):
    def ShuffleBurn(self):
        random.shuffle(self.cards)
        del self.cards[-100:]

deck = DeckWrapper(deck_builder(card_factory))

# AttributeError: __delitem__
# shoe1 = Shoe1(deck_builder(card_factory, 3))
# shoe1.ShuffleBurn()
# print(len(shoe1))

shoe2 = Shoe2(deck_builder(card_factory, 3))
shoe2.ShuffleBurn()
print(len(shoe2))
