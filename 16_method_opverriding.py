class Hridoy:
    def speak(self):
        print("Good Morning")

class Student(Hridoy):#Inheritance
    def speak(self):    # Overrides parent method
        print("Good Afternoon !")

s = Student()
s.speak()       