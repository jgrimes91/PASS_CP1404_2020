from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty

class AnimalShelter(App):
    # animal names needs to be in the outer scope for the Spinner to use it
    # Lindsay does this too in his Spinner demo so this is OK!
    animal_names = ListProperty()

    def build(self):
        self.title = "Paws & Claws Animal Shelter"
        self.root = Builder.load_file("animal_shelter.kv")
        # Create an object for each Cat and Dog using the relevant classes!
        anakin = #
        padme = #
        yoda = #
        leia = #
        solo = #
        chewy = #

        # Create a dictionary from the animal objects
        # Use the format {'Anakin':anakin} - relating the animal name to it's object
        self.animals = #animal dictionary

        # Get the animal names as a list - we'll need this to build a drop down menu
        self.animal_names = #
        return self.root

    def get_animal_info(self, animal_name):
        animal = # get the animal's object from the dictionary using it's name
        self.root.ids.output_label.text = # update the description using the .speak() method
        self.root.ids.animal_image.source = # update the image

##                                                              ##
## THE CLASSES FROM LAST WEEK - Nothing to do below this point! ##
##                                                              ##
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
