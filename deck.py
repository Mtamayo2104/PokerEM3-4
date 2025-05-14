from pyclbr import Class
import random

class Card(object):
    RANKS= ["2","3","4","5","6","7","8","9","10","J","Q","K", "A"]
    SUITS = ["♣", "♦", "♥","♠"]
    def __init__(self, suit, rank):
        """
        Validates that both the suit and rank are valid values (from SUITS and RANKS class attributes)
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._suit = suit
        self._rank = rank


    def __eq__(self, other):
        """
        Compare two cards for equality based on their ranks.

        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compare if this card's rank is greater than another card's rank.

        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Return a readable string representation of the card.
        """
        return (f"{self._rank}{self._suit}")

    def __repr__(self):
        """
        Return the official string representation of the card.
        """
        return self.__str__()

    @property
    def suit(self):
        """
        get the card's suit

        """
        return self._suit
    @property
    def rank(self):
        """
        get the card's rank
        """
        return self._rank

class Deck:
    def __init__(self):
        """
        Creates a complete deck by generating all possible combinations of
        suits and ranks as defined in Card.SUITS and Card.RANKS.
        The deck is ordered by suit first, then by rank according to
        the ordering in these class attributes.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))


    def __str__(self):
        """
        Provides a complete view of all cards in the deck in their current order,
        formatted as a standard Python list string representation.
        """
        return str(self._deck)

    def shuffle(self):
        """
        shuffle the deck into a random order

        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deals the first card from the deck (position 0) by removing it from the deck
        and returning it. This follows standard dealing behavior from the top of the deck

        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())