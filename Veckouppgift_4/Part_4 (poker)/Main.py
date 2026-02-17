import random
from collections import Counter

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_details(self):
        return f"{self.suit} {self.rank}"


def get_card_deck():
    suit_ranks = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    deck = []

    for suit in suit_ranks:
        for rank in ranks:
            deck.append(Card(suit, rank))
    random.shuffle(deck)
    return deck

def draw_cards(deck, number_of_cards):
    drawn_cards = deck[:number_of_cards]
    deck = deck[number_of_cards:]
    return drawn_cards, deck

def get_rank_value(rank):
    if rank == "Jack":
        return 11
    elif rank == "Queen":
        return 12
    elif rank == "King":
        return 13
    elif rank == "Ace":
        return 14
    else:
        return rank

def check_hand(hand):
    ranks = [get_rank_value(card.rank) for card in hand]
    suits = [card.suit for card in hand]

    ranks.sort()

    # Count duplicates
    rank_counts = {}
    for r in ranks:
        rank_counts[r] = rank_counts.get(r, 0) + 1

    counts = sorted(rank_counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = ranks == list(range(ranks[0], ranks[0] + 5))

    # Special straight: A,2,3,4,5
    if ranks == [2, 3, 4, 5, 14]:
        is_straight = True

    # Check hands
    if is_straight and is_flush and max(ranks) == 14:
        return "Royal Flush"
    elif is_straight and is_flush:
        return "Straight Flush"
    elif counts == [5]:
        return "Five of a Kind" # only possible when cards are drawn from randomized options and not from actual deck
    elif counts == [4, 1]:
        return "Four of a Kind"
    elif counts == [3, 2]:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif counts == [3, 1, 1]:
        return "Three of a Kind"
    elif counts == [2, 2, 1]:
        return "Two Pair"
    elif counts == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card"


# make deck
deck = get_card_deck()

hand =[]

# draw cards
hand, deck = draw_cards(deck, 5)
for card in hand:
    print(card.card_details())

print(check_hand(hand))
#print("\nRemaining Deck:")
#for card in deck:
#    print(card.card_details())