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


class Player:

    def __init__(self, name):
        self.name = name
        self.allcards = []

    def add_cards(self,newCards):
        if type(newCards) == type([]):
            #add multiple Cards aka List
            self.allcards.extend(newCards)
        else:
            #Add just 1 card
            self.allcards.append(newCards)

    def remove_one(self):
        return self.allcards.pop()

    def __str__(self):
        return f'Player {self.name} has {len(self.allcards)} cards.'


if __name__ == '__main__':
    print("Game Starting")

    player1 = Player('One')
    player2 = Player('Two')

    deck = Deck()
    deck.shuffle()

    while len(deck.allcards) != 0:
        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())

    print("Dealing Completed")
    print(len(player1.allcards))
    print(len(player2.allcards))

    game_on = True

    round = 0

    while game_on:
        round += 1
        print('round : ', round)

        if len(player1.allcards) == 0:
            print("Player 2 won")
            game_on = False
            break
        if len(player2.allcards) == 0:
            print("Player 1 won")
            game_on = False
            break


        #Game is still on

        at_war = True
        card_player1 = []
        card_player2 = []

        card_player1.append(player1.remove_one())
        card_player2.append(player2.remove_one())

        while at_war:
            if card_player1[-1].value > card_player2[-1].value:
                #Player 1 Card > Player 2 Card, player 1 gets all the cards
                player1.add_cards(card_player1)
                player1.add_cards(card_player2)
                print('1 if')

                print('len deck p1 - ', len(player1.allcards))
                print('len deck p2 - ', len(player2.allcards))
                at_war = False
                break

            if card_player1[-1].value < card_player2[-1].value:
                #Player 1 Card < Player 2 Card, player 2 gets all the cards

                player2.add_cards(card_player1)
                player2.add_cards(card_player2)
                print('2 if')
                print('len deck p1 - ', len(player1.allcards))
                print('len deck p2 - ', len(player2.allcards))

                at_war = False
                break

            else:
                print("War!")
                if len(player1.allcards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins!\n Player One Loses!")
                    game_on = False
                    break

                elif len(player2.allcards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins!\nPlayer One Loses!")
                    game_on = False
                    break
                    # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for num in range(5):
                        card_player1.append(player1.remove_one())
                        card_player2.append(player2.remove_one())


