class students:
    def __init__(self,name):
        self.name=name
        self.cgpa=3.5
        self.__password="123456"
    
students = students ('Sharifs')
print (students.name)
print(students.CGPA)