from random import random as r

test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


def place_marker(board, marker, position):
    if (0 < position <= 9):
        board[position] = marker
    else:
        print('Insert into a valid position 1-9')


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal

def choose_first():
    first = 1
   #print(first)

    if first == 1:
        print('You are player1')
        return "Player 1"
    elif first == 2:
        return "Player 2"
    else:
        return "cenas"


def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False

def full_board_check(board):

    for i in range(board):
        if space_check(board,board[i]):
            return False
    return True

def player_choice(board):
    position = int(input('Position to play: '))

    if space_check(board,position):
        return position

def replay():
    again = input('Do you want to play again: (Y or N): ')

    if again == 'Y':
        return True
    elif again == 'N':
        return False



def game():
    global test_board
    print("Welcome to Tic Tac Toe!")


    while True:

        choose_first()

        player1, player2 = player_input()
        print(player1, player2)

        game_on=True

        while game_on:
            display_board(test_board)
            place_marker(test_board, player1, player_choice(test_board))
            display_board(test_board)

            if win_check(test_board, 'X'):
                game_on = False
                if player1 == 'X':
                    print("Player1 venceu")
                    break
                if player2 == 'X':
                    print("Player2 venceu")
                    break

            if win_check(test_board, 'O'):
                game_on = False
                if player1 == 'O':
                    print("Player1 venceu")
                    break
                if player2 == 'O':
                    print("Player2 venceu")
                    break
            place_marker(test_board, player2, player_choice(test_board))

            if win_check(test_board, 'X'):
                game_on = False
                if player1 == 'X':
                    print("Player1 venceu")
                    break
                if player2 == 'X':
                    print("Player2 venceu")
                    break

            if win_check(test_board, 'O'):
                game_on = False
                if player1 == 'O':
                    print("Player1 venceu")
                    break
                if player2 == 'O':
                    print("Player2 venceu")
                    break

        if not replay():
            break
        test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

if __name__ == '__main__':
    game()
