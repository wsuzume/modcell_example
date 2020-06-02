# game.ipynb ---------
# ---


import random

def dice():
    return random.randint(1, 6)

class Game:
    def __init__(self):
        self.name = 'BackGammon'
        
    def dice(self):
        return dice(), dice()

# ---
# --------- game.ipynb
# ../module_notebook/animal.ipynb ---------
# ---


class Mammal:
    def __init__(self):
        self.response = 'Hello.'
        
    def hello(self):
        print(self.response)

class Dog(Mammal):
    def __init__(self):
        self.response = 'Henlo, gimme some food.'

class Cat(Mammal):
    def __init__(self):
        self.response = 'Meowning.'

# ---


class Bird:
    def __init__(self):
        self.response = 'Hello.'
    
    def hello(self):
        print(self.response)

class Pigeon(Bird):
    def __init__(self):
        self.response = 'Coo coo.'

class Crow(Bird):
    def __init__(self):
        self.response = 'Caw!'

# ---
# --------- ../module_notebook/animal.ipynb
