# Snake and Ladder Game

import random

class SnakeAndLadder:
    def _init_(self):
        self.board = self.create_board()
        self.players = {}
        self.current_player = None

    def create_board(self):
        board = {i: i for i in range(1, 101)}
        snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

        for start, end in snakes.items():
            board[start] = end
        for start, end in ladders.items():
            board[start] = end

        return board

    def add_player(self, name):
        self.players[name] = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, name):
        roll = self.roll_dice()
        print(f"{name} rolled a {roll}")
        self.players[name] += roll

        if self.players[name] > 100:
            self.players[name] = 100

        self.players[name] = self.board.get(self.players[name], self.players[name])
        print(f"{name} is now on square {self.players[name]}")

    def check_winner(self):
        for player, position in self.players.items():
            if position == 100:
                return player
        return None

    def play_game(self):
        while True:
            for player in self.players.keys():
                self.current_player = player
                self.move_player(player)
                winner = self.check_winner()
                if winner:
                    print(f"{winner} wins!")
                    return

# Example of how to play the game
game = SnakeAndLadder()
game.add_player("Player 1")
game.add_player("Player 2")
game.play_game()
