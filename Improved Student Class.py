# Use of Person class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)



class Student:
    
    def __init__(self, person, password):
        self.person = person
        self.password = password
        self.projects = []
    def get_name(self):
        return self.person.full_name()
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
    def check_password(self, supply):
        if self.password == supply:
            return True
        else:
            return False
        
        
#################################################
# Student adds code where appropriate    
    
# implementation of average_age
def average_age(person_list, current_year):
    total_age = 0
    count = 0.0
    average_age = 0
    for p in person_list:
        total_age += p.age(current_year)
        count += 1.0
    if count != 0.0:
        average_age = total_age/count
    return average_age    

def assign(students, full, password, project):
    for p in students:
        exist = False
        if p.get_name() == full and p.check_password(password):
            for t in p.get_projects():
                if t == project:
                    exist = True
            if exist == False:
                p.add_project(project) 
                    
                     
###################################################
# Testing code
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print joe.get_projects()
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print joe.get_projects()

print john.get_projects()
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print john.get_projects()
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print john.get_projects()
