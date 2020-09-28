from kivy.app import App
from kivy.lang import Builder


class RectangleCalculator(App):
    def build(self):
        self.title = "Rectangle Calculator"
        self.root = Builder.load_file("rectangle_calculator.kv")
        return self.root

    def calculate_area(self, length, width):
        try:
            length = int(length)
            width = int(width)
            if width < 0 or length < 0:
                self.root.ids.output_label.text = "Length and width can't be negative, enter valid numbers"
            else:
                area = length * width
                self.root.ids.output_label.text = "Area = " + str(area) + "cm^2"
        except:
            self.root.ids.output_label.text = "Enter valid numbers for length and width"

    def calculate_perimeter(self, length, width):
        try:
            length = int(length)
            width = int(width)
            if length < 0 or width < 0:
                self.root.ids.output_label.text = "Length or width is negative, enter positive numbers"
            else:
                perimeter = 2 * (length + width)
                self.root.ids.output_label.text = "Perimeter = " + str(perimeter) + "cm"
        except:
            self.root.ids.output_label.text = "Enter valid numbers for length and width"


RectangleCalculator().run()
