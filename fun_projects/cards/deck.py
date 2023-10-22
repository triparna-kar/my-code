import random

suits = ['club', 'spade', 'diamond', 'heart']
ranks = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':11,
    'Q':12,
    'K':13,
}


class Card():
    """
    This class defines the properties of a single card
    """
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value


class Deck():
    """
    This class defines the functionality, i.e, operations to be done cards
    """
    def __init__(self):
        # initialise all the cards using Cards class.
        self.cards = list()
        for suit in suits:
            for rank, value in ranks.items():
                self.cards.append(Card(suit, rank, value))
        print("\n\n### Cards Created! ###")
        self.print_cards()
        
                
    def shuffle(self):
        # shuffle cards
        random.shuffle(self.cards)
        print("\n\n### Cards Shuffled! ###")
        self.print_cards()

    def sort_suit(self, suit_list):
        # implement sorting algorithm to sort cards by suit and rank (same suit together)
        length = len(suit_list)        # self.cards is a list
        for i in range(1, length):
            j = i-1
            key = suit_list[i]
            while(j>=0 and suit_list[j].value>key.value):
                suit_list[j+1] = suit_list[j]
                j = j - 1
                suit_list[j+1] = key
        return suit_list

    def sort_deck(self):
        suit_club = list()
        suit_diamond = list()
        suit_spade = list()
        suit_heart = list()
        for item in self.cards:
            if item.suit == 'club':
                suit_club.append(item)
            if item.suit == 'diamond':
                suit_diamond.append(item)
            if item.suit == 'spade':
                suit_spade.append(item)
            if item.suit == 'heart':
                suit_heart.append(item)
        self.sort_suit(suit_club)
        self.sort_suit(suit_diamond)
        self.sort_suit(suit_spade)
        self.sort_suit(suit_heart)
        self.cards = list()
        for item in suit_club:
            self.cards.append(item)
        for item in suit_diamond:
            self.cards.append(item)
        for item in suit_spade:
            self.cards.append(item)
        for item in suit_heart:
            self.cards.append(item)                        
        print("\n\n### Cards Sorted! ###")
        self.print_cards()

    def print_cards(self):
        print("\n### Printing Cards Order --->")
        position = 0
        for item in self.cards:
            print("Position: {pos}, Suit: {suit}, Rank: {rank}, Value: {val}".format(
                        pos=position, 
                        suit=item.suit, 
                        rank=item.rank, 
                        val=item.value
                        )
                )
            position += 1


mydeck = Deck()
mydeck.shuffle()
mydeck.sort_deck()