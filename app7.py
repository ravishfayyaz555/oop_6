# Access Modifiers

class Employee:
    def __init__(self,name,salary,ssn):
      self.name = name      # Public
      self.salary = salary  # Protected
      self.ssn =  ssn      # Private

emp = Employee("Areeba",20000,"123-4567")
print(emp.name)