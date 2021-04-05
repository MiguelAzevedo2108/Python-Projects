import random

#global variables

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nive',
          'Ten', 'Jack', 'Queen', 'King', 'Ace']

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nive': 9,
          'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:
    def __init__(self, suit,rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.allcards = []

        for i in suits:
            for j in ranks:
                #Create the card object
                card = Card(i,j)
                self.allcards.append(card)

    def shuffle(self):
        random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()


deck = Deck()
deck.shuffle()


if __name__ == '__main__':
    print("Running")

    for i in deck.allcards:
        print(i.__str__())
