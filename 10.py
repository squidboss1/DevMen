import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.suit}"

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        # wartości
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # kolory w kartach
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        # karty
        cards = []

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                cards.append(card)

        return cards
        # return [Card(value, suit) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            print("Error: The deck is empty.")


deck = Deck()

print("Shuffled deck:")
for card in deck.cards:
    print(card)

print("\nDealing cards:")
for _ in range(5):
    dealt_card = deck.deal()
    if dealt_card:
        print(f"Dealt card: {dealt_card}")
    else:
        break
