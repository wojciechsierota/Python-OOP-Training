import random
 
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
 
    def __repr__(self):
        return f"{self.rank}{self.suit}"
 
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♠', '♥', '♦', '♣']
        self.cards = [Card(r, s) for r in ranks for s in suits]
   
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        hand = []
        for _ in range(n):
            if self.cards:
                card = self.cards.pop()
                hand.append(card)

        return hand
    
class HandEvaluator:
    def evaluate(self, hand):
        ranks = [c.rank for c in hand]
        suits = [c.suit for c in hand]


        counts = {}
        for r in ranks:
            counts[r] = counts.get(r, 0) + 1

        v = sorted(counts.values(), reverse=True)

        is_flush = len(set(suits)) == 1

        if is_flush:
            return "Flush"
        
        if v[0] == 4:
            return "Four of a Kind"
        
        if v[0] == 3 and v[1] == 2:
            return "Full House"
        
        if v[0] == 3:
            return "Three of a Kind"
        
        if v[0] == 2 and v[1] == 2:
            return "Two Pair"
        
        if v[0] == 2:
            return "Pair"
        
        return "High Card"
    

my_deck = Deck()

my_deck.shuffle()

hand = my_deck.draw(5)
print("Your hand:", hand)

evaluator = HandEvaluator()
print("Hand rank:", evaluator.evaluate(hand))
