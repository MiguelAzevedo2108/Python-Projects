import random

naipes = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

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

        if card.rank == 'Ace':
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

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.ajust_ace()



def hit_or_stand(deck,hand):
    global playing

    while(1):
        x = input("Hit or Stand? Enter h or s ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stand Dealer's Turn")
            playing = False
        else:
            print("Sorry, i did not understand that. Hit h or s only!")
            continue
        break


def showSome(player,dealer):

    #Shows only 1 dealer's card
    print("\n Dealer's Hand: ")
    print("First Card Hidden!")
    print(dealer.cards[1])

    #Show all (2 cards) players hand/cards
    print("\n Players Hand")
    for i in player.cards:
        print(i)

def showAll(player,dealer):
    #show all dealers card
    print("\n Dealer Hand")
    for i in dealer.cards:
        print(i)

    #calculate and diplay the value

    print(f"Value of Dealer's hand is: {dealer.hand_value}")

    #show all players card

    print("\n Players Hand")
    for i in player.cards:
        print(i)

    print(f"Value of Player's hand is: {player.hand_value}")


def player_bust(player, dealer, chips):
    print("Bust Player")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("Player Wins")
    chips.win_bet()


def dealer_bust(player,dealer,chips):
    print("PLayer Wins! Dealer Busted")
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.win_bet()


def push(player,dealer):
    print("Deaçer and player tie! Push")




if __name__ == '__main__':

    print("Welcome to BlackJack")

    deck = Deck()
    deck.shuffle()

    #Setup the Players cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Setup the Players cards
    player_chips = Chips()

    #Prompt the Pleyer for their bet
    take_bet(player_chips)

    #Show cards (but keep 1 hidden)
    showSome(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        showSome(player_hand,dealer_hand)

        if player_hand.hand_value > 21:
            player_bust(player_hand,dealer_hand,player_chips)
            break

        if player_hand.hand_value < 21:
            while dealer_hand.hand_value < 17:
                hit(deck,dealer_hand)

            showAll(player_hand,dealer_hand)

            if dealer_hand.hand_value > 21:
                dealer_bust(player_hand,dealer_hand,player_chips)

            elif dealer_hand.hand_value > player_hand.hand_value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.hand_value < player_hand.hand_value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)

        print("\n PLayer total chips are at: {}".format(player_chips.total))

        new_game = input("Play again (Y/N):")

        if new_game[0].lower() == 'y':
            playing = True
        else:
            print("Thank you for playing ")
            break


