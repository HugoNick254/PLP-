class Player:
    #"A class containing some of my favourite basketball players."

    #"Attributes include: name, age, position played, team playing for"

    def __init__(self, name, age, position, team):

        self.name = name 
        self.age = age
        self.position = position
        self.team = team
    

    def get_info(self):
        print(f"This is {self.name}, {self.age} years old, a {self.position} for {self.team}.")


class NBAPlayer(Player):
    #"A class showing the status of the players in relation to the NBA."

    def __init__(self, name, age, position, team, is_active):
            super().__init__(name, age, position, team)
            self.status = "Active" if is_active else "Retired"

    def get_status_info(self):
            return f"{self.name} is currently {self.status}"


player1 = NBAPlayer("Shai Gilgeous-Alexander", "27", "Point Guard", "Oklahoma City Thunder", True)
player2 = NBAPlayer("Nikola Jokic", "30", "Centre", "Denver Nuggets", True)
player3 = NBAPlayer("Kevin Durant", "36", "Small Forward", "Houston Rockets", True)
player4 = NBAPlayer("Carmelo Anthony", "41", "Power Forward", "New York Knicks", False)
player5 = NBAPlayer("Michael Jordan", "62", "Shooting Guard", "Chicago Bulls", False)

print(player1.get_info())
print(player1.get_status_info())

print(player4.get_info())
print(player4.get_status_info())


# Activity 2

class Vehicle:
    def __init__(self, make, model):
        self.model = model
        self.make = make

    def get_info(self):
        return f"This is a {self.make} {self.model}."
    
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def move(self):
        return f"{self.year} {self.make} {self.model} is driving off."
    
class Boat(Vehicle):
    def __init__(self, make, model, is_motorised):
        super().__init__(make, model)
        self.is_motorised = is_motorised 

    def move(self):
        propeller = "engine" if self.is_motorised else "sail"
        return f"{self.make} {self.model} moves through water by {propeller}."
    
class Plane(Vehicle):
    def __init__(self, make, model, number_of_engines):
        super(). __init__(make, model)
        self.number_of_engines = number_of_engines

    def move(self):
        return f"{self.make} {self.model} flies through the air on {self.number_of_engines} engines."
    

my_car = Car("Toyota", "Mark II", "1993")
my_boat = Boat("Sea Ray", "240 Sundancer", True)
my_plane = Plane("Boeing", "747", "4")

print(my_car.move())
print(my_boat.move())
print(my_plane.move())
