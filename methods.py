class Vehicle: # Made a Base Class
    def __init__(self, name):
        self.name = name
    
    def make_sound(self): # Made a method
        print(f"{self.name} makes generic vehicle sound.")

    def describe(self):
        print(f"This is a vehicle called {self.name}.")


class Car(Vehicle):
    def make_sound(self):
        print(f"{self.name} goes honk honk!")


class Train(Vehicle):
    def make_sound(self):
        print(f"{self.name} goes Choo Choo!")

my_car = Car("Honda Civic")
my_car.describe()


        

