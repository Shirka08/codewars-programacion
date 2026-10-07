class Person:
    def __init__ (self, name, age): 
        self.age = age
        self.name = name
    
    @property 
    def info(self):
        return self.name + "s age is " + str(self.age)