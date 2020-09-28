from kivy.app import App
from kivy.lang import Builder
import random

class DiceRoller(App):
    def build(self):
        self.title = "PASS Dice Roller"
        self.root = Builder.load_file("dice_roller.kv")
        return self.root

    def roll_dice(self):
        result = random.randint(1, 6)
        self.root.ids.output_label.text = str(result)

DiceRoller().run()
