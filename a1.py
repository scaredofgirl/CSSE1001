# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name: Ernest Chan Lam Hong
# Student Number: 48617101
# ----------------

# Write your classes and functions here

def num_hours() -> float:
    """return the number of hrs spend on this
    """
    time_spent = 30.0
    return time_spent

def generate_initial_board() -> list[str]:
    """to make an empty board

    using the funciton make an empty board of 8x8

    return:
        list: 8x8 empty board
    """
    BOARD_SIZE = 8
    BLANK_PIECE = '-'
    empty_board = []
    for column in range(BOARD_SIZE):
        empty_board.append((BLANK_PIECE)*8)
    
    return empty_board



def is_column_full(column: str) -> bool:
    """checking if the colume is full

    checking the columns for any empty spaces

    parameters:
        column (str): the column to check

    return:
        T/F based on if there are any empty spaces in the column
    """
    for each_space in column:
        if each_space == '-':
            return False
    return True



def is_column_empty(column: str) -> bool:
    """checking if the colume is empty

    checking the columns if there are 8 empty spaces

    parameters:
        column (str): the column to check

    return:
        T/F based on if there are 8 empty spaces in the column
    """
    total_spaces = 0
    for each_space in column:
        if each_space == '-':
            total_spaces += 1
    if total_spaces == 8:
        return True
    else:
        return False



def display_board(board: list[str]) -> None:
    """take the board and print it

    taking the input from the board and displaying the board
    add the column num at the bottom of the display

    parameters:
        current_board (list): the list that shows the state of the board

    return:
        a display of the board

    preconditions:
        8 strings with 8 characters each
    """
    #precondition
    count = 0
    for column in board:
        count += 1
    if not (count == 8 and len(board) == 8):
        return False
    
    for column in range(len(board)):
        display = ['|']
        for value in range(len(board[column])):
            display.append(str(board[value][column]) + '|')
        
        print(''.join(display))

    number_row = [' ']
    for number in range(len(board[0])):
        number_row += str(number + 1) + ' '
    print(''.join(number_row))
    


        
def check_input(command: str) -> bool:
    """check if the input is well formatted

    take the input and compare it to the list of commands

    parameters:
        command (str): input of the user

    return:
        T/F (bool): t/f based on if the input is well formatted
    """
    action = ('A', 'R')
    command = command.upper()
    INVALID_FORMAT_MESSAGE = "Invalid command. Enter 'h' for valid command format"
    INVALID_COLUMN_MESSAGE = f"Invalid column, please enter a number between 1 and {BOARD_SIZE} inclusive"

    if not command:
        print(INVALID_FORMAT_MESSAGE)
        return False
    
    elif len(command) == 1:
        if command[0] == 'H' or command[0] == 'Q':
            return True  
        print(INVALID_FORMAT_MESSAGE)
        return False
    
    elif len(command) != 2:
        print(INVALID_FORMAT_MESSAGE)
        return False
    
    elif command[0] not in action:
        print(INVALID_FORMAT_MESSAGE)
        return False

    elif int(command[1]) not in range(1, 9):
        print(INVALID_COLUMN_MESSAGE)
        return False
        
    elif command[0] in action:
        if command[1].isdigit() and int(command[1]) in range(1, 9):
            return True        

    print(INVALID_FORMAT_MESSAGE)
    return False



def get_action() -> str:
    """repeatedly ask the user for the correct input

    repeatedly asking the user for an input, giving the approriate response

    return:
        (str): give the next input if the correct input is entered and wrong if the wrong input is entered
    """
    INVALID_FORMAT_MESSAGE = "Invalid command. Enter 'h' for valid command format"
    while True:
        choice = input("Please enter action (h to see valid commands): ")
        if check_input(choice):
            return choice


def add_piece(board: list[str], piece: str, column_index: int) -> bool:
    """add a peice to the board

    takes the user input and add to the board

    parameters:
        board (list): the current board state
        piece (str): the piece to add to the board
        column_index (int): the column to add the peice to

    return:
        t/f (bool): True if the piece can be added. False if cannot

    precondition:
        board has 8 string with 8 characters
        column_index = range(0, 8)
        len(piece) == 1
    """
    #predconditions
    if not len(piece) == 1:
        return False
    if not column_index >= 0 and column_index < 8:
        return False
    count = 0
    for column in board:
        count += 1
    if not (count == 8 and len(board) == 8):
        return False

    FULL_COLUMN_MESSAGE = "You can't add a piece to a full column!"
    empty_space_num = 0
    position_count = 0
    column = list(board[column_index])
            
    if '-' not in column:
        print(FULL_COLUMN_MESSAGE)
        return False

    for position, value in enumerate(column):
        if value == '-':
            position_count = position         
    column[position_count] = piece
    board[column_index] = ''.join(column)
    return True



def remove_piece(board: list[str], column_index: int) -> bool:
    """removes the bottom piece at the bottom of the column

    removes the last piece from the column and moves all the piece down by 1

    parameters:
        board (list): the current board
        column_index (int): the column to edit

    return:
        (bool): True if column not empty and chaneg the column. False if empty

    precondition:
        board has 8 string with 8 characters
        column_index = range(0, 8)
    """
    #preconditions
    if column_index not in range(8):
        return False
    count = 0
    for column in board:
        count += 1
    if not (count == 8 and len(board) == 8):
        return False

    EMPTY_COLUMN_MESSAGE = "You can't remove a piece from an empty column!"
    column = list(board[column_index])

    if column[7] == '-':
        print(EMPTY_COLUMN_MESSAGE)
        return False

    last_number = column.pop()
    column.insert(0, '-')
    board[column_index] = ''.join(column)
    return True


        
def check_win(board: list[str]) -> Optional[str]:
    """check if there are any win con

    check for vertical, horizontal and disgonal matches

    parameters:
        board(list): current board

    return:
        Optional(str): shows which player is the winner if any. 'O' if player 1 and 'X' if player 2 and '-' if both win

    preconditions:
        board has 8 strings with 8 characters
        each character should only be '-', 'O' or 'X'
    """
    #preconditions
    count = 0
    correct_characters = ('-', 'O', 'X')
    for column_index in board:
        if not (len(column_index) == 8 and len(board) == 8):
            break
    for column_index in board:
        for letter in column_index:
            if letter not in correct_characters:
                break
                
    winner = []

    #checking for vertical
    for column_index in range(len(board)):
        column = list(board[column_index])
        for letter in range(len(column) - 3):
            if column[letter] == 'O' and column[letter + 1] == 'O' and column[letter + 2] == 'O' and column[letter + 3] == 'O':
                winner.append('O')
            if column[letter] == 'X' and column[letter + 1] == 'X' and column[letter + 2] == 'X' and column[letter + 3] == 'X':
                winner.append('X')

    #checking horizontal
    for column_index in range(len(board[0]) - 3):
        for letter in range(len(board[0])):
            if board[column_index][letter] == 'O' and board[column_index + 1][letter] == 'O' and board[column_index + 2][letter] == 'O' and board[column_index + 3][letter] == 'O':
                winner.append('O')
            if board[column_index][letter] == 'X' and board[column_index + 1][letter] == 'X' and board[column_index + 2][letter] == 'X' and board[column_index + 3][letter] == 'X':
                winner.append('X')
                
    #checking diagonal
    for column_index in range(len(board[0]) - 3):
        for letter in range(len(board) - 3):
            #left to right downward & right to left upwards
            if (board[column_index][letter] == 'O' and board[column_index + 1][letter + 1] == 'O' and board[column_index + 2][letter + 2] == 'O' and board[column_index + 3][letter + 3] == 'O'):
                winner.append('O')
            if (board[column_index][letter] == 'X' and board[column_index + 1][letter + 1] == 'X' and board[column_index + 2][letter + 2] == 'X' and board[column_index + 3][letter + 3] == 'X'):
                winner.append('X')
            #left to right upwards & right to left downwards
            if (board[column_index][letter + 3] == 'O' and board[column_index + 1][letter + 2] == 'O' and board[column_index + 2][letter + 1] == 'O' and board[column_index + 3][letter] == 'O'):
                winner.append('O')
            if (board[column_index][letter + 3] == 'X' and board[column_index + 1][letter + 2] == 'X' and board[column_index + 2][letter + 1] == 'X' and board[column_index + 3][letter] == 'X'):
                winner.append('X')
            
    #check who won
    if len(winner) == 1:
        return winner[0]
    elif len(winner) >= 2:
        if 'O' in winner:
            if 'X' in winner:
                return '-'
    else:
        return None


def next_turn(turn: str) -> str:
    """get the turn count and display the correct turn message

    parameters:
        turn (str): the turn numebr so we know whose turn it is

    return: printing player 1 or player 2 according to the turn count
    """
    if turn % 2 == 0:
        print(PLAYER_2_MOVE_MESSAGE)
                
    else:
        print(PLAYER_1_MOVE_MESSAGE)



def winning_msg() -> str:
    """show the ending msg

    return:
        (str): returnt the ending msg
    """
    play_again = input(CONTINUE_MESSAGE)
    if play_again == 'y':
        play_game()      


        
def play_game() -> None:
    """run thru the different steps of the gameplay

    return:
        the connect 4 game
    """    
    PLAYER_1_MOVE_MESSAGE = "Player 1 to move"
    PLAYER_2_MOVE_MESSAGE = "Player 2 to move"
    PLAYER_1_VICTORY_MESSAGE = "Player 1 wins!"
    PLAYER_2_VICTORY_MESSAGE = "Player 2 wins!"
    DRAW_MESSAGE = "Its a Draw!"
    CONTINUE_MESSAGE = "Would you like to play again? (y/n): "
    ENTER_COMMAND_MESSAGE = "Please enter action (h to see valid commands): "
    HELP_MESSAGE = """Valid commands: 
- aX: Add piece to top of column X (X must be a valid integer)
- rX: Remove a piece from bottom of column X (X must be a valid integer)
- h: Display help text
- q: Quit current game\n"""

    board = generate_initial_board()
    turn = 1
    continue_loop = False

    while not check_win(board):
        if not continue_loop:
            display_board(board)
            if turn % 2 != 0:
                print(PLAYER_1_MOVE_MESSAGE)
            else:
                print(PLAYER_2_MOVE_MESSAGE)
        
        user_input = get_action().upper()
        continue_loop = False

        if check_input(user_input):
            user_input = list(user_input)
            if user_input[0] == 'H':
                print(HELP_MESSAGE)
                continue
            if user_input[0] == 'Q':
                return
            if user_input[0] == 'A':
                piece = 'X' if turn % 2 != 0 else 'O'
                if not add_piece(board, piece, int(user_input[1])-1):
                    continue_loop = True
                    continue
            if user_input[0] == 'R':
                if not remove_piece(board, int(user_input[1])-1):
                    continue_loop = True
                    continue

        if check_win(board):
            display_board(board)
            winner = check_win(board)
            if winner == 'X':
                print(PLAYER_1_VICTORY_MESSAGE)
            elif winner == 'O':
                print(PLAYER_2_VICTORY_MESSAGE)
            elif winner == '-':
                print(DRAW_MESSAGE)
            break

        turn += 1

def main() -> None:
    """Main function to start the game."""
    while True:
        play_game()
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
