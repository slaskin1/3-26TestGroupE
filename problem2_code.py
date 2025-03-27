def determine_board_state(input_list):
    # Step 1: Validate input type
    if not isinstance(input_list, list) or len(input_list) != 3:
        raise Exception("Input must be a list of 3 lists")

    for row in input_list:
        if not isinstance(row, list) or len(row) != 3:
            raise Exception("Each row must be a list of 3 integers")
        if not all(isinstance(cell, int) for cell in row):
            raise Exception("Each cell must be an integer")

    # Step 2: Define helper function to check win conditions
    def is_winner(board, player):
        # Check rows and columns
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    # Step 3: Check for winning conditions
    player1_win = is_winner(input_list, 1)
    player2_win = is_winner(input_list, 2)

    if player1_win:
        print("Player 1 win")
        return True
    elif player2_win:
        print("Player 2 win")
        return True
    else:
        print("No winner")
        return False
# Example usage:
# if __name__ == "__main__":
#     board = [
#         [0, 1, 2],
#         [0, 1, 0],
#         [2, 1, 0]
#     ]

#     result = determine_board_state(board)
#     print("Result:", result)