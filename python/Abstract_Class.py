#1. Create an abstract class with abstract and non-abstract methods
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):        # abstract method
        pass

    def fuel_type(self):   # non-abstract method
        print("Vehicle uses fuel")

#2. Create a subclass for abstract class & access non-abstract methods
class Bike(Vehicle):

    def start(self):
        print("Bike started")
#3. Create an instance for the child class and call abstract methods
b = Bike()
b.start()   # abstract method implementation

#4. Create an instance for the child class and call non-abstract methods
b = Bike()
b.fuel_type()   # non-abstract method from abstract class


