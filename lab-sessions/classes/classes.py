class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def info(self):
        print(self.name, self.age, self.height)
    
    def change_age(self, new_age):
        self.age = new_age
    
