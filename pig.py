import random

class Die:
    def __init__(self):
        random.seed(0)  # Set the seed for reproducibility

    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player_index = 0
        self.target_score = 100
        self.die = Die()  # Create a single Die instance

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        turn_total = 0

        while True:
            print(f"{current_player.name}'s turn. Current score: {current_player.score}, Turn total: {turn_total}")
            action = input("Enter 'r' to roll or 'h' to hold: ")

            if action == 'r':
                rolled_value = self.die.roll()  # Use the same Die instance
                print(f"You rolled a {rolled_value}")

                if rolled_value == 1:
                    print("You rolled a 1! Turn ends with no points.")
                    break
                else:
                    turn_total += rolled_value
            elif action == 'h':
                current_player.add_score(turn_total)
                break

        if current_player.score >= self.target_score:
            print(f"{current_player.name} wins with a score of {current_player.score}!")
            return True  # Game over
        return False  # Game continues

    def play(self):
        while True:
            if self.play_turn():
                break  # Exit the loop if someone wins
            self.switch_player()

if __name__ == "__main__":
    game = Game()
    game.play()
    pass
    
