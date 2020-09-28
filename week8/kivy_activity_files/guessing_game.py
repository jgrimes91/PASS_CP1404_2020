from kivy.app import App
from kivy.lang import Builder
import random


class GuessingGame(App):
    def build(self):
        self.title = "Guess the Secret Number!"
        self.root = Builder.load_file("guessing_game.kv")
        self.secret_number = random.randint(1, 10)
        return self.root

    def check_guess(self, guess):
        try:
            self.root.ids.input_text.text = ''
            guess = int(guess)
            if guess > 10 or guess < 1:
                self.root.ids.output_label.text = "Invalid number! Must be between 1-10"
            elif guess == self.secret_number:
                self.root.ids.output_label.text = "YAY! " + str(
                    guess) + " is the secret number!\nPress \"Reset Game\" to play again"
                print("hello")
            else:
                self.root.ids.output_label.text = "The secret number isn't " + str(guess) + "! Try again."
                print("yes")
        except:
            self.root.ids.output_label.text = "Enter a number between 1-10!"

    def reset_game(self):
        self.secret_number = random.randint(1, 10)
        self.root.ids.output_label.text = "Game reset!\nEnter a number between 1-10!"

    def exit_game(self):
        GuessingGame().stop()


GuessingGame().run()
