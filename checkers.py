# import random, resize, and swapaxes from numpy
# Define build_board function
    # use random.choice
    # return the board
# Define get_count function
    # use string_search to return a board of T/F
    # use .sum() on T/F board to get sum of T
    # return result
# Define change_size function
    # use resize with input to change size
    # return resized board
# Define pivot_axes function
    # use swapaxes to flip board axes
    # return the swapped board
# Check if file is running on main, if so print a notification to not do that





from numpy import random
from numpy import resize
from numpy import swapaxes


def build_board(board_size):
    board = random.choice(['Empty', 'Red', 'Black'], (board_size, board_size))
    return board


def get_count(board, string_search):
    cond_grid = (board == string_search)
    return cond_grid.sum()


def change_size(board, new_size):
    resize_board = resize(board, (new_size, new_size))
    return resize_board


def pivot_axes(board):
    pivot_board = swapaxes(board, 0, 1)
    return pivot_board


if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")
