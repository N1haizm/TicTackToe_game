class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None
    def display_board(self):
        print("\n")
        print("-" * 9)
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print(" | ".join(row))
            print("-" * 9)
    def get_player_input(self):
        while True:
            try:
                position = int(input(f"Player {self.current_player}, choose a position (1-9): ")) - 1
                if 0 <= position < 9 and self.board[position] == " ":
                    return position
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                self.winner = self.current_player
                return True
        return False
    def check_draw(self):
        return " " not in self.board
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    def play(self):
        while not self.winner and not self.check_draw():
            self.display_board()
            position = self.get_player_input()
            self.board[position] = self.current_player
            if self.check_winner():
                self.display_board()
                print(f"Player {self.winner} wins!")
            else:
                self.switch_player()
        if not self.winner:
            print("It's a draw!")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                self.__init__()
                self.play()
                break
            elif play_again == 'no':
                print("Alrighty then, bye-bye! thanks for playing!")
                break
            else:
                print("Unknown input!\n")
                continue
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe in Python.\nPlayers get ready! Player X is moving first..")
    game = TicTacToe()
    game.play()
