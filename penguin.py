# penguin.py
# J. Andrew Yurick
# November 9, 2026
# Class representing a penguin

class Penguin:
    def __init__(self, sample_number, species, body_mass):
        self.sample_number = sample_number
        self.species = species
        self.body_mass = body_mass

    def display_info(self):
        #display the sample number
        print(f"Sample Number: {self.sample_number}")
        #display the species
        print(f"Species: {self.species}")
        #display the body mass
        print(f"Body Mass: {self.body_mass} g")
    