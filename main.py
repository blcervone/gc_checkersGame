def game():
    import checkers

    board_size = int(input("What size is the board you'd like to play on? >"))
    new_board = checkers.build_board(board_size)
    print()
    print(new_board)

    empty_count = checkers.get_count(new_board, 'Empty')
    red_count = checkers.get_count(new_board, 'Red')
    black_count = checkers.get_count(new_board, 'Black')

    print()
    print(f"There are {empty_count} Empty cells on the board!")
    print(f"There are {red_count} Red cells on the board!")
    print(f"There are {black_count} Black cells on the board!")
    print()

    new_size = int(input("Please enter the new board size: >"))
    print()
    resize_board = checkers.change_size(new_board, new_size)
    print(resize_board)
    print()

    swap_axes = checkers.pivot_axes(new_board)
    print("Here is the original board with swapped axes:")
    print()
    print(swap_axes)

if __name__ == '__main__':
    game()
