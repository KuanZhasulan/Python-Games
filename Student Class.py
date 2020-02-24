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

###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

instructors = [joe, john, stephen, scott]
print average_age(instructors, 2013)

instructors.pop() # get rid of Scott and his bogus age
print average_age(instructors, 2013)

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print joe_student.get_name()
print joe_student.check_password("qwert")
print joe_student.check_password("TopSecret")

print joe_student.get_projects()
joe_student.add_project("Create practice exercises")
print joe_student.get_projects()
joe_student.add_project("Implement Minecraft")
print joe_student.get_projects()




####################################################
# Output of testing code 

#44.5
#50.6666666667