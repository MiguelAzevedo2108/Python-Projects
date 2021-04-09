import random

naipes = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, naipe, rank):
        self.naipe = naipe
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.naipe


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for naipe in naipes:
            for rank in ranks:
                card = Card(naipe, rank)
                self.deck.append(card)

    def __str__(self):
        deck = ''
        for i in self.deck:
            deck += '\n' + i.__str__()
        return 'This deck has:' + deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.hand_value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.hand_value += values[card.rank]

        if card.ranks == 'Ace':
            self.aces += 1


    def ajust_ace(self):

        while self.aces > 0 and self.hand_value > 21:
            self.hand_value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Insert your bet: '))
        except:
            print('Please insert a valid amount')
        else:
            if chips.bet > chips.total:
                print('Your bet cant exceed', chips.total)
            else:
                break


def hit(deck, hand):
    pass


if __name__ == '__main__':
    print('PyCharm')

    deck = Deck()
    deck.shuffle()
    print(deck.__str__())
    print('End')
    hand = Hand()
    hand.add_card(deck.deal())
    for i in hand.cards:
        print(i)
    print(hand.hand_value)
