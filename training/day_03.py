 # classes
 # let's write a class that represents a car

class Car:
    def __init__(self, brand, model, color, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} is now running")
        else:
            print(f"{self.brand} {self.model} is already running")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} is now stopped")
        else:
            print(f"{self.brand} {self.model} is already stopped")

    def accelerate(self, increase):
        if self.is_running:
            self.speed += increase
            print(f"{self.brand} {self.model} is now going {self.speed} km/h")
        else:
            print(f"{self.brand} {self.model} is not running")


    def display_details(self):
        print(f"{self.brand} {self.model} is a {self.color} car that is going {self.speed} km/h")



my_car = Car("Toyota", "Supra", "White", 120)
my_car.display_details()
my_car.start()
my_car.accelerate(60)
my_car.display_details()
my_car.stop()


