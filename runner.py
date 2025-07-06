import tic_tac_toe as ttt

def print_board(board):
    for row in board:
        print(" ".join([cell if cell is not None else "_" for cell in row]))
    print()


def main():
    board = [[ttt.EMPTY, ttt.EMPTY, ttt.EMPTY],
             [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY],
             [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]]

    while not ttt.terminal(board):
        print_board(board)
        if ttt.player(board) == ttt.X:
            print("AI is thinking...")
            move = ttt.minimax(board)
        else:
            move = None
            while move not in ttt.actions(board):
                try:
                    i, j = map(int, input("Enter row and column (0-2): ").split())
                    move = (i, j)
                except ValueError:
                    print("Invalid input. Please enter two numbers between 0 and 2.")

        board = ttt.result(board, move)

    print_board(board)
    winner = ttt.winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
