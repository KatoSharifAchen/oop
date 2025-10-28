class students:
    def __init__(self,name):
        self.name=name
        self.cgpa=3.5
        self.__password="1234"
    
students = students ('Sharifs')
print (students.name)
print(students.CGPA)