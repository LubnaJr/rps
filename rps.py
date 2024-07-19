import random
import string
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.nextMove = ' '

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()

    def move(self):
        if self.nextMove not in moves:
            self.nextMove = random.choice(moves)
        return self.nextMove

    def learn(self, my_move, their_move):
        self.nextMove = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        if self.nextMove not in moves:
            self.nextMove = random.choice(moves)
        return self.nextMove

    def learn(self, my_move, their_move):
        move_i = moves.index(my_move) + 1
        self.nextMove = moves[move_i % 3]


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        self.nextMove = input("Enter your move: Rock, Paper,"
                              " or Scissors\n").lower()
        while self.nextMove not in moves:
            self.nextMove = input("invalid input\nEnter your move: Rock, "
                                  "Paper, or Scissors\n").lower()
        return self.nextMove


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, game_rounds):
        self.p1 = p1
        self.p2 = p2
        self.game_rounds = int(game_rounds)

    def play_round(self):
        print(f"Player 1 score: {self.p1.score}\n"
              f"Player 2 score: {self.p2.score}")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.p1.score += 1
        elif move1 == move2:
            print("Game tied!")
        else:
            print("Player 2 wins the round!")
            self.p2.score += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(self.game_rounds):
            print(f"Round {round}:")
            self.play_round()
        print(f"Final score: [{self.p1.score}  :  {self.p2.score}] ")
        if self.p1.score > self.p2.score:
            print("palayer 1 wins the game")
        elif self.p1.score < self.p2.score:
            print("palayer 2 wins the game")
        else:
            print("It's a draw!")
        print("Game over!")


def play_again():
    game_mood = ''
    modes = ['easy', 'medium', 'hard', 'exit']
    while game_mood not in modes:
        game_mood = input("Enter the game mode to paly: Easy, Medium,"
                          " or Hard, or Enter Exit to quit the game\n").lower()
    return game_mood


if __name__ == '__main__':
    state = play_again()
    while state != 'exit':
        choice = ''
        while choice not in ['1', '3']:
            choice = input("Enter 1 to play a fast game, Enter"
                           " 3 to play a three rounds game\n")
        if state == 'easy':
            game = Game(HumanPlayer(), CyclePlayer(), choice)
            game.play_game()
        elif state == 'medium':
            game = Game(HumanPlayer(), RandomPlayer(), choice)
            game.play_game()
        elif state == 'hard':
            game = Game(HumanPlayer(),  ReflectPlayer(), choice)
            game.play_game()
        state = play_again()
