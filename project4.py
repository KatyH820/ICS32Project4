from columns import *
from copy import deepcopy


def input_board_size() -> tuple:
    """
    Read two lines of input that describe the size of game board
    Return the input as a tuple
    """
    row = int(input())
    col = int(input())
    if row < 4 or col < 3:
        raise ValueError
    return row, col


def input_board_field(row) -> list:
    """
    Read lines of input determine how the initial board will look like.
    if the field is to begin empty, the word EMPTY will appear alone in the return list.
    if the field is to begin with specified contents, the word CONTENTS along with contents
    of the board will be in the return list. The return list will be a list of string"""
    field_content = []
    for i in range(row+1):
        field_content.append(input())
        if field_content[0].strip() == "EMPTY":
            break
    return field_content


def input_command() -> list:
    """Return command input in list"""
    return input().split(' ')


def create_empty_board(row: int, column: int) -> list[list[str]]:
    """Given row and column, create and return a empty board"""
    game_board = []
    lst = []
    for j in range(column):
        lst.append(' ')
    for i in range(row+2):
        game_board.append(deepcopy(lst))
    return game_board


def create_content_board(field_content: list, column: int) -> list[list[str]]:
    """Given field_content and column, create and return a content board"""
    game_board = [[' ']*column, [' ']*column]
    for line in field_content[1:]:
        game_board.append(list(line))
    return game_board


def create_initial_board(field_content: list, row: int, col: int) -> list[list[str]]:
    """Create and return the initial board"""
    if field_content[0] == 'EMPTY':
        initial_board = create_empty_board(row, col)
    else:
        initial_board = create_content_board(field_content, col)
    return initial_board


def action(game_state: GameState, command: list, new_faller=None) -> None or Faller:
    """Given game_state, user command perform the action"""
    if (len(command) == 1 and command[0].strip() == '' and new_faller != None) or game_state._matching:
        if not(game_state._matching):
            game_state.enter_action(new_faller)
        else:
            game_state.enter_action()
    elif command[0] == 'F' and 1 <= int(command[1]) <= len(game_state._game_board[0]):
        color_list = command[2:]
        col_num = int(command[1])-1
        if game_state.count_empty_space_in_col(col_num) <= 2:
            game_state.game_over_action(False)
        if not(game_state.faller_on_gameboard()):
            new_faller = Faller(color_list, col_num)
            game_state.add_faller(new_faller)
    elif command[0].strip() == 'R' and new_faller != None:
        game_state.rotate_action(new_faller)
    elif command[0].strip() == '<' and new_faller != None:
        if game_state.can_move(new_faller, -1):
            game_state.move_action(new_faller, -1)
    elif command[0].strip() == '>' and new_faller != None:
        if game_state.can_move(new_faller, 1):
            game_state.move_action(new_faller, 1)
    elif command[0].strip() == 'Q':
        game_state.stop_running()
    if new_faller != None:
        return new_faller


def run():
    """
    Run the game. Ask user input and create a game board that is to be turn in to the game state.
    The game then begin by repeatedly do two things: Display the field, and read command
    from the user.
    """
    row, col = input_board_size()
    board_field = input_board_field(row)
    game_board = create_initial_board(board_field, row, col)
    game_state = GameState(game_board)
    while game_state.game_is_running():
        if game_state.faller_on_gameboard() or game_state._matching:
            game_state.draw_game_board()
            command = input_command()
            action(game_state, command, new_faller)
        else:
            game_state.draw_corrected_format_board()
            command = input_command()
            if (n := action(game_state, command)) != None:
                new_faller = n


if __name__ == '__main__':
    run()
