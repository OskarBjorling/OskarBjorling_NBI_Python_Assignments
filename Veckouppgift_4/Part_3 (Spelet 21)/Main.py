import random

def calculate_hand():
    hand = []
    while sum(hand) <= 21:
        card = random.randint(1,13)
        hand.append(card)

    print("Summa ", sum(hand))
    print("Hand", hand)

calculate_hand()