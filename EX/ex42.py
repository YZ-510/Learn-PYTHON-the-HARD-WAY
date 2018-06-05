## Animal is-a object
class Animal:
    pass

## Dog is-a Animal    
class Dog(Animal):
    def __init__(self, name):
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name

## Person is-a object        
class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None
    
## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

## Fish is-a object
class Fish:
    pass

## Salmon is-a Fish    
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog    
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet, satan is-a cat
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()