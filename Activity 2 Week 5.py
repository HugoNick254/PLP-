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
