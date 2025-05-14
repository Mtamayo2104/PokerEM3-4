from deck import Deck, Card


class PokerHand:
    def __init__(self, deck):
        """
        Initialize a new poker hand by dealing 5 cards from a deck.

        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        The cards in this hand (read-only property).

        """
        return self._cards

    def __str__(self):
        """
        Return string representation of the hand.

        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        True if all cards are of the same suit (a flush).

        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def number_matches(self):
        """
        Count of matching ranks (used to detect pairs/trips/quads).

        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        True if hand contains exactly one pair.

        """
        if self.number_matches == 2:# more simple
            return True
        return False


    @property
    def is_two_pair(self):
        """
        True if hand contains two different pairs.

        """
        return self.number_matches == 4  # more advanced

    @property
    def is_trips(self):
        """
        True if hand contains three of a kind.

        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        True if hand contains four of a kind.

        """
        return self.number_matches == 12

    @property
    def _is_full_house(self):
        """
        True if hand contains a full house (three of a kind and a pair).

        """
        return self.is_trips and self.is_pair

    @property
    def is_straight(self):
        """
        True if hand contains five sequential ranks (a straight).

        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4


    # deck = Deck()
# deck.shuffle()
# hand = PokerHand(deck)
# print(hand)
count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle ()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
        print(hand)
    count += 1

print(f"probability of a straight is a {100*matches/count}%")
