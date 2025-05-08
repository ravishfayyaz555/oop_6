# using self

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student1 = Student("Ravish fayyaz",25)
student1.display()