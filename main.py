import random


board=['_','_','_','_','_','_','_','_','_']
winner=None
start = None
computer_choice = ""
user_choice = ''
game_on=True

#print the game board
def print_board(board):
    print(board[0] +'|' +board[1]+ '|' +board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

#computer_choice =""
#choosing X or O
def choice():
    global user_choice, computer_choice
    user_choice = input("Enter your choice either X or O: ").upper()
    if user_choice == 'X':
        computer_choice = 'O'
    else:
        computer_choice = 'X'
    print(f'User will play {user_choice} and computer will play {computer_choice}')

def starting():
    global start
    start_choice=random.randint(1,2)
    if start_choice == 1:
        start="computer"
        print("Computer will start")
    else:
        start="user"
        print("User will start")

def play_game_computer(board, computer_choice):
    index=random.randint(1,9)
    if board[index-1]=='_':
        board[index - 1] =  computer_choice

    else:
        print("Opps Already Played")

def play_game_user(board, user_choice):
    indexu = int(input("Enter a number between 1 and 9: "))
    if board[indexu - 1] == '_':
        board[indexu - 1] = user_choice

    else:
        print("Opps Already Played")


def winner_check(board):
    global winner, game_on
    combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] and board[a] != '_':
            winner = board[a]
            game_on = False


def check_tie(board):
    global game_on
    if '_' not in board:
        print("It's a tie")
        game_on = False

choice()
starting()
print(f"computer_choice: {computer_choice}")
print(f"user_choice: {user_choice}")
while game_on:
    print_board(board)
    if start == 'computer':
        play_game_computer(board, computer_choice)
        winner_check(board)
        if winner:
            print('Computer wins!')
        check_tie(board)
        start = 'user'
    else:
        play_game_user(board, user_choice)
        winner_check(board)
        if winner:
            print('You win! Congratulations')
        check_tie(board)
        start = 'computer'







