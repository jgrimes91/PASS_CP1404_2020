from kivy.app import App
from kivy.lang import Builder


class CarCounter(App):
    def build(self):
        self.title = "Car Counter"
        self.root = Builder.load_file("car_counter.kv")
        self.number_of_cars = 0
        return self.root

    def handle_increment(self, increment):
        self.number_of_cars = self.number_of_cars + increment
        if self.number_of_cars < 0:
            self.number_of_cars = 0
        self.root.ids.output_label.text = "There are {} cars in the carpark".format(self.number_of_cars)


CarCounter().run()
