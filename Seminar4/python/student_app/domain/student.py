from domain.person import Person


class Student(Person):#Comparable
    generalId = 0


    def __init__(self, name, age):
        super().__init__(name, age)
        self.id = Student.generalId
        Student.generalId += 1

    def getId(self):
        return self.id

    def __str__(self):
        return "Students [age=" + str(super().getAge()) + ", name=" + super().getName() + ", id=" + str(self.id) + "]"

    def __lt__(self, obj): 
        return ((self.age) < (obj.age)) 
  
    def __gt__(self, obj): 
        return ((self.age) > (obj.age)) 
  
    def __le__(self, obj): 
        return ((self.age) <= (obj.age)) 
  
    def __ge__(self, obj): 
        return ((self.age) >= (obj.age)) 
  
    def __eq__(self, obj): 
        return (self.age == obj.age) 