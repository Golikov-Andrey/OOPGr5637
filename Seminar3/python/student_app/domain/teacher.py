
from domain.person import Person


class Teacher(Person):
    def __init__(self, firstName, age, acadDegree):
        super().__init__(firstName, age)
        self.acadDegree = acadDegree