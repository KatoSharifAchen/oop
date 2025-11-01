class students:
    def __init__(self,name):
        self.name=name
        self.cgpa=3.5
        self.__password="123456789"
    
students = students ('Sharif')
print (students.name)
print(students.CGPA)