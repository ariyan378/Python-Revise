class Cat:
    def speak(self):
        print("Meow!")

class Dog: #same method different output this is known as polymorphism
    def speak(self): 
        print("Woof!")

for animal in [Cat(), Dog()]:
    animal.speak()