from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty


class AnimalShelter(App):
    animal_names = ListProperty()

    def build(self):
        self.title = "Paws & Claws Animal Shelter"
        self.root = Builder.load_file("animal_shelter.kv")
        anakin = Cat('Anakin', '2 year', 'domestic short hair', 'male', 250, 'anakin.jpg')
        padme = Cat('Padme', '3 month', 'tabby X', 'female', 300, 'padme.jpg')
        yoda = Cat('Yoda', '10 year', 'domestic short hair', 'male', 150, 'yoda.jpg')
        leia = Dog('Leia', '2 year', 'Staffy X', 'female', 250, 'leia.jpg')
        solo = Dog('Solo', '8 month', 'German Shepard X', 'male', 350, 'solo.jpg')
        chewy = Dog('Chewy', '5 year', 'Rhodesian Ridgeback X', 'male', 250, 'chewy.jpg')
        self.animals = {'Anakin': anakin, 'Padme': padme, 'Yoda': yoda, 'Leia': leia, 'Solo': solo, 'Chewy': chewy}
        self.animal_names = self.animals.keys()
        return self.root

    def get_animal_info(self, animal_name):
        animal = self.animals[animal_name]
        self.root.ids.output_label.text = animal.speak()
        self.root.ids.animal_image.source = animal.imageFile


class Cat:
    def __init__(self, name, age, breed, gender, adoptionFee, imageFile):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender
        self.adoptionFee = adoptionFee
        self.imageFile = imageFile

    def __str__(self):
        return "{} - {} old {} cat".format(self.name, self.age, self.gender)

    def speak(self):
        return ("Meow! My name is {} and I’m a {} old {}. The humans tell me\
        \nthat I’m a {}, and you can adopt me for ${}. Could you give me the\
        \npurrfect home?".format(self.name,
                                 self.age, self.gender, self.breed, self.adoptionFee))


class Dog:
    def __init__(self, name, age, breed, gender, adoptionFee, imageFile):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender
        self.adoptionFee = adoptionFee
        self.imageFile = imageFile

    def __str__(self):
        return "{} - {} old {} dog".format(self.name, self.age, self.gender)

    def speak(self):
        return ("Woof! My name is {} and I’m a {} old {}. I am told\
        \nthat I’m a {}, and can be adopted for ${}. Could you be my\
        \nforever family?".format(self.name,
                                  self.age, self.gender, self.breed, self.adoptionFee))


AnimalShelter().run()
