class person():
    def __init__(self, name, age, school, skin_color):
        self.name = name
        self.age = age
        self.school = school
        self.skin_color = skin_color
    def print_person(self):
        print(self.name)
        print(self.age)
        print(self.school)
        print(self.skin_color)
        
        
        
p = person("Manav", 15, "DESC", "Brown")
p.print_person()