import random
hair_color = ['black', 'white', 'red', 'green', 'brown', 'yellow']

class Student:
    def __init__(self, name, age, grade, country):
        self.name = name
        self.age = age
        self.grade = grade
        self.country = country
        self.backpack = []
        self.hair_color = random.choice(hair_color)
    def __str__(self):
        s = ''
        s += "Name: " + self.name + "\n"
        s += "Grade: " + self.grade + "\n"
        s += "Country: " + self.country + "\n"
        return s
    
    def put(self, item):
        self.backpack.append(item)
        
    def open_backpack(self):
        return self.backpack
    
    def show_age(self):
        if self.name == "Mystic":
            return random.randrange(1, 100)
        else:
            return self.age
    
    def show_hair(self):
        return self.hair_color
    def change_color(self, color):
        self.hair_color = color
        
Zhasik = Student("Zhassulan", 18, "12E", "Kazakhstan")
print Zhasik
print "Initial hair color: "+Zhasik.show_hair()
Zhasik.change_color("aqua")
print "Changed hair color: "+ Zhasik.show_hair()
Zhasik.put('pen')
print Zhasik.open_backpack()
